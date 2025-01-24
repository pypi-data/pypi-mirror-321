#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define NPY_NO_DEPRECATED_API 7
#include "numpy/arrayobject.h"
#include "numpy/npy_math.h"
#include <sqlfront.h>
#include <sybdb.h>


/* #define VERBOSE 1 */

/*
  Python module which uses the FreeTDS BCP implementation to
  bulk import numpy arrays into an SQL Server database table
  with one column per array.
*/

#if ((PY_MAJOR_VERSION == 2) && (PY_MINOR_VERSION < 7)) || (PY_MAJOR_VERSION < 2)
/* For python < 2.7, we use the CObject API */
#define PTR_FROM_OBJECT(x)    PyCObject_AsVoidPtr((x))
#define OBJECT_FROM_PTR(x, y) PyCObject_FromVoidPtr((x), (y))
#define DESTR_GET_PTR(x)      (x)
#else
/* For python >= 2.7, we use the Capsule API */
#define PTR_FROM_OBJECT(x)    PyCapsule_GetPointer((x), NULL)
#define OBJECT_FROM_PTR(x, y) PyCapsule_New((x), NULL, ((PyCapsule_Destructor) y))
#define DESTR_GET_PTR(x)      PyCapsule_GetPointer((PyObject *) x, NULL)
#endif

#define PY_ARRAY_UNIQUE_SYMBOL _PYBCP

/* Whether freetds is initialised */
static int need_init = 1;

/* Most recent error message */
#define MAXLEN 100
static char last_err[MAXLEN];
static char last_msg[MAXLEN];
static char full_error[10*MAXLEN];

/* Macro for reporting errors as python exceptions */
#define SQL_EXCEPTION(x) {sprintf(full_error, "%s\n%s\n%s", (x), last_err, last_msg); PyErr_SetString(_pybcpError, full_error);}

/*
  FreeTDS error handling routines
*/
int msg_handler(DBPROCESS *dbproc, DBINT msgno, int msgstate, int severity, 
		char *msgtext, char *srvname, char *procname, int line)
{									
  enum {changed_database = 5701, changed_language = 5703 };	
       
  if (msgno == changed_database || msgno == changed_language) 
    return 0;

  if (msgno > 0)strncpy(last_msg, msgtext, MAXLEN-1);

#ifdef VERBOSE
  fflush(stdout);
  fflush(stderr);

  if (msgno > 0) {

    fprintf(stderr, "\n\nMsg %ld, Level %d, State %d\n", 
	    (long) msgno, severity, msgstate);
    
    if (strlen(srvname) > 0)
      fprintf(stderr, "Server '%s', ", srvname);
    if (strlen(procname) > 0)
      fprintf(stderr, "Procedure '%s', ", procname);
    if (line > 0)
      fprintf(stderr, "Line %d", line);
    
    fprintf(stderr, "\n\t");
  }
  fprintf(stderr, "%s\n\n", msgtext);
#endif  

  return 0;							
}

int err_handler(DBPROCESS * dbproc, int severity, int dberr, int oserr, 
		char *dberrstr, char *oserrstr)
{
  strncpy(last_err, dberrstr, MAXLEN-1);

#ifdef VERBOSE									
  if (dberr)
    {							
      fflush(stdout);
      fflush(stderr);
      fprintf(stderr, "\nError\n"); 
      fprintf(stderr, "%s\n\n", dberrstr);
      fflush(stderr);
    }  
  else
    {
      fflush(stdout);
      fflush(stderr);
      fprintf(stderr, "\nDB-LIBRARY error:\n");
      fprintf(stderr, "%s\n", dberrstr);
      fflush(stderr);
    }
#endif
  return INT_CANCEL;						
}

/* New python exception for error reporting */
static PyObject *_pybcpError;

/* Function prototypes */
static PyObject *_pybcp_connect(PyObject *self, PyObject *args);
static PyObject *_pybcp_bulk_insert(PyObject *self, PyObject *args);
static PyObject *_pybcp_exec_sql(PyObject *self, PyObject *args);
static PyObject *_pybcp_get_columns(PyObject *self, PyObject *args);

/* Method table for the module */
static PyMethodDef _pybcpMethods[] = {
  {"connect",     _pybcp_connect,     METH_VARARGS, "Connect to database"},
  {"bulk_insert", _pybcp_bulk_insert, METH_VARARGS, "Bulk insert data from numpy arrays"},
  {"exec_sql",    _pybcp_exec_sql,    METH_VARARGS, "Execute SQL command"},
  {"get_columns", _pybcp_get_columns, METH_VARARGS, "Get names and types of columns in a table"},
  {NULL, NULL, 0, NULL}        /* Sentinel */
};


/* Module definition struct for Python 3 only */
#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "_pybcp",
  NULL,
  -1,
  _pybcpMethods
};
#endif


/* Initialise the module */
#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC PyInit__pybcp(void)
#else
PyMODINIT_FUNC init_pybcp(void)
#endif
{
  PyObject *m;
 
  /* Make sure NumPy is imported and initialised */
  import_array();

#if PY_MAJOR_VERSION >= 3
  m = PyModule_Create(&moduledef);
  if (m == NULL)
    return NULL;
#else
  m = Py_InitModule("_pybcp", _pybcpMethods);
  if (m == NULL)
    return;
#endif

  _pybcpError = PyErr_NewException("_pybcp.SQLError", NULL, NULL);
  Py_INCREF(_pybcpError);
  PyModule_AddObject(m, "SQLError", _pybcpError);
#if PY_MAJOR_VERSION >= 3
  return m;
#endif
}


/*
  Struct with connection info
*/
typedef struct
{
  DBPROCESS *dbproc;
  LOGINREC  *login;
} db_connection;


/* 
   Clean up DB connection struct -
   this is called directly if setting up the DB connection
   fails, or from the destructor function below if the
   python Capsule/CObject storing the pointer is deallocated.
*/
void db_connection_close(db_connection *db)
{
  if(db->dbproc)dbclose(db->dbproc);
  if(db->login)free(db->login);
  free(db);
}


/* 
   Python destructor for the db_connection struct -
   if we're using the PyCapsule API this gets passed a
   pointer to a Capsule. We need to extract the pointer to
   the db_connection and call the real destructor.
*/
void db_connection_destr(void *obj)
{
  db_connection_close(DESTR_GET_PTR(obj));
}


/*
   Connect to the database

   Parameters (all strings):
   
   - Username
   - Password
   - FreeTDS server name
   - Context database name

*/
static PyObject *_pybcp_connect(PyObject *self, PyObject *args)
{
  char *user;
  char *pass;
  char *server;
  char *database;
  RETCODE erc;
  db_connection *dbcon = NULL;

  /* Clear message buffers */
  last_msg[0] = 0;
  last_err[0] = 0;

  /* Get parameter values */
  if (!PyArg_ParseTuple(args, "ssss", &user, &pass, &server, &database))
    {
      SQL_EXCEPTION("Don't understand arguments!");
      goto cleanup;
    }

  /* Allocate output struct */
  dbcon = malloc(sizeof(db_connection));
  if(!dbcon)
    {
      SQL_EXCEPTION("Can't allocate memory for connection!");
      goto cleanup;
    }
  dbcon->login  = NULL;
  dbcon->dbproc = NULL;

  /* Init FreeTDS */
  if(need_init)
    {
      if(dbinit() == FAIL)
	{
	  SQL_EXCEPTION("Can't initialise database access library!");
	  goto cleanup;
	}
      need_init = 0;
    }

  /* Set error handlers */
  dberrhandle(err_handler);
  dbmsghandle(msg_handler);
  
  /* Allocate login data structure */
  dbcon->login = dblogin();
  if(!dbcon->login)
    {
      SQL_EXCEPTION("Unable to allocate login structure\n");
      goto cleanup;
    }

  /* Set user name and password */
  DBSETLUSER(dbcon->login, user);
  DBSETLPWD(dbcon->login, pass);
  
  /* Connect */
  dbcon->dbproc = dbopen(dbcon->login, server);
  if(!dbcon->dbproc)
    {
      SQL_EXCEPTION("Unable to connect to server\n");
      goto cleanup;
    }
	
  /* Select the context database */
  erc = dbuse(dbcon->dbproc, database);
  if(erc == FAIL)
    {
      SQL_EXCEPTION("Unable to set context database\n");
      goto cleanup;
    }

  /* Return a pointer to the db_connection struct as a PyCObject */
  PyObject *obj = OBJECT_FROM_PTR((void *) dbcon, &db_connection_destr);
  return obj;
  
 cleanup:
  if(dbcon) db_connection_close(dbcon);
  return NULL;
}


/*
  Struct to describe a column in a table
*/
typedef struct
{
  size_t         size;
  PyArrayObject *array;
  int            npytype;
  int            sqltype;
  char          *boundvar;
} column;


/*
   Bulk insert data

   Parameters:
  
   DB connection - pycobject
   Table name    - string
   Data          - list of numpy arrays

*/
static PyObject *_pybcp_bulk_insert(PyObject *self, PyObject *args)
{
  PyObject *db_obj;
  char     *table;
  PyObject *data_list;
  PyObject *callback;
  db_connection *dbcon = NULL;
  column *cols = NULL;
  int ncol=0, icol;
  int nrow;
  int bcp_started = 0;
  int have_callback;
  int ncallback;

  /* Clear message buffers */
  last_msg[0] = 0;
  last_err[0] = 0;

  /* Get parameter values */
  if (!PyArg_ParseTuple(args, "OsOOi",
			&db_obj,
			&table,
			&data_list,
			&callback, 
			&ncallback))
    {
      SQL_EXCEPTION("Don't understand arguments!");
      goto cleanup;
    }

  /* Get pointer to DB connection struct */
  dbcon = PTR_FROM_OBJECT(db_obj);

  /* Sanity check on input */
  if(!PyList_Check(data_list))
    {
      SQL_EXCEPTION("Data arrays must be supplied as a list!");
      goto cleanup;
    }
  ncol = PyList_Size(data_list);

  /* Check if we have a callback */
  if(callback == Py_None)
    {
      /* No callback */
      have_callback = 0;
    }
  else
    {
      /* Check supplied object is callable */
      if (!PyCallable_Check(callback)) 
	{
	  SQL_EXCEPTION("Callback parameter must be callable!");
	  goto cleanup; 
	}
      have_callback = 1;      
    }


  /* Allocate storage for column metadata */
  cols = malloc(sizeof(column)*ncol);
  if(!cols)
    {
      SQL_EXCEPTION("Unable to allocate memory!");
      goto cleanup;  
    }
  else
    {
      for(icol=0;icol<ncol;icol+=1)
	{
	  cols[icol].array    = NULL;
	  cols[icol].boundvar = NULL;
	}
    }

  /* Extract column info */
  nrow = 0;
  for(icol=0;icol<ncol;icol+=1)
    {
      /* Get a contiguous data array corresponding to this column */
      PyObject *data_obj = PyList_GetItem(data_list, icol);
      if(!PyArray_Check(data_obj))
	{
	  SQL_EXCEPTION("Data list must be list of numpy arrays!");
	  goto cleanup;   
	}
      cols[icol].array = (PyArrayObject *) 
	PyArray_GETCONTIGUOUS((PyArrayObject *) data_obj); /* New reference */
      /* Check for native endian */
      if(PyArray_ISBYTESWAPPED(cols[icol].array))
	{
	  SQL_EXCEPTION("Data array must be native endian!");
	  goto cleanup;
	}
      /* Determine data type for this column */
      int type = PyArray_TYPE((PyArrayObject *) cols[icol].array);
      if(PyArray_EquivTypenums(type, NPY_INT32))
	{
	  cols[icol].npytype = NPY_INT32;
	  cols[icol].sqltype = SYBINT4;
	  cols[icol].size    = 4;
	}
      else if(PyArray_EquivTypenums(type, NPY_INT64))
	{
	  cols[icol].npytype = NPY_INT64;
	  cols[icol].sqltype = SYBINT8;
	  cols[icol].size    = 8;
	}
      else if(PyArray_EquivTypenums(type, NPY_FLOAT32))
	{
	  cols[icol].npytype = NPY_FLOAT32;
	  cols[icol].sqltype = SYBREAL;
	  cols[icol].size    = 4;
	}
      else if(PyArray_EquivTypenums(type, NPY_FLOAT64))
	{
	  cols[icol].npytype = NPY_FLOAT64;
	  cols[icol].sqltype = SYBFLT8;
	  cols[icol].size    = 8;
	}
      else if(PyArray_EquivTypenums(type, NPY_STRING))
	{
	  cols[icol].npytype = NPY_STRING;
	  cols[icol].sqltype = SYBCHAR;
	  cols[icol].size    = PyArray_ITEMSIZE((PyArrayObject *) cols[icol].array);
	}
      else
	{
	  /* A type we can't deal with */
	  SQL_EXCEPTION("Data array has unsupported type!");
	  goto cleanup; 
	}
      /* Check dimensions */
      if(PyArray_NDIM((PyArrayObject *) cols[icol].array) != 1)
	{
	  SQL_EXCEPTION("Data arrays must be one dimensional!");
	  goto cleanup; 
	}
      if(icol==0)
	{
	  nrow = (int) (*PyArray_DIMS((PyArrayObject *) cols[icol].array));
	}
      else
	{
	  if(nrow != (int) (*PyArray_DIMS((PyArrayObject *) cols[icol].array)))
	    {
	      SQL_EXCEPTION("Data arrays must all be the same size!");
	      goto cleanup;  
	    }
	}
      /* Allocate bound variable */
      if(!(cols[icol].boundvar = malloc(cols[icol].size)))
	{
	  SQL_EXCEPTION("Unable to allocate memory for bound variable");
	  goto cleanup;  
	}
    }

#ifdef VERBOSE
  /* Write column info */
  printf("ncol = %d\n", ncol);
  printf("nrow = %d\n", nrow);
  for(icol=0;icol<ncol;icol+=1)
    printf("type = %d\n", cols[icol].sqltype);
#endif  

  RETCODE erc;

  /* Initialise the bulk copy operation */
  erc = bcp_init(dbcon->dbproc, table, NULL, "errorfile", DB_IN);
  if(erc == FAIL)
    {
      SQL_EXCEPTION("bcp_init() call failed!");
      goto cleanup;
    } 
  else
    {
      bcp_started = 1;
    }

  /* Bind the columns */
  for(icol=0; icol<ncol; icol+=1)
    {
      DBINT len;
      if(cols[icol].sqltype == SYBCHAR)
	len = cols[icol].size;
      else
	len = -1;
      erc = bcp_bind(dbcon->dbproc, (BYTE *) cols[icol].boundvar,
		     0, len, NULL, 0, cols[icol].sqltype, icol+1);
      if(erc == FAIL)
	{
	  SQL_EXCEPTION("bcp_bind() call failed!");
	  goto cleanup;
	}
    }

  /* Set bulk copy options */
  char rpb[200];
  //sprintf(rpb,"ROWS_PER_BATCH=%d, TABLOCK", nrow);
  sprintf(rpb,"TABLOCK");
  erc = bcp_options(dbcon->dbproc, BCPHINTS, (BYTE *) rpb, (int) strlen(rpb));
  if(erc == FAIL)
    {
      SQL_EXCEPTION("Unable to set bulk copy options!");
      goto cleanup;
    }

  /* Import the data */
  int irow;
  for(irow=0; irow<nrow; irow+=1)
    {
      for(icol=0; icol<ncol; icol+=1)
	{
	  size_t sz  = cols[icol].size;
	  char *src  = ((char *) PyArray_BYTES(cols[icol].array)) + (irow*sz);
	  char *dest = cols[icol].boundvar;
	  memcpy(dest, src, sz);
	}
      if(bcp_sendrow(dbcon->dbproc)==FAIL)
	{
	  SQL_EXCEPTION("Unable to send row to server\n");
	  goto cleanup;
	}
      if(have_callback && (irow % ncallback == 0))
	{
	  /* Call callback periodically */
	  PyObject *arglist = Py_BuildValue("(i)", irow);
	  PyObject_CallObject(callback, arglist);
	  Py_DECREF(arglist);
	}
    }

  if(bcp_done(dbcon->dbproc)<0)
    {
      SQL_EXCEPTION("Bulk copy failed\n");
      goto cleanup;
    }

  /* Deallocate column data */
  for(icol=0;icol<ncol;icol+=1)
    Py_DECREF(cols[icol].array);
  free(cols);
  
  /* Done */
  Py_RETURN_NONE;

 cleanup:
  if(bcp_started)bcp_done(dbcon->dbproc);
  if(cols)
    {
      for(icol=0;icol<ncol;icol+=1)
	{
	  if(cols[icol].array)Py_DECREF(cols[icol].array);
	  if(cols[icol].boundvar)free(cols[icol].boundvar);
	}
      free(cols);
    }
  return NULL;
}


/*
  Execute an SQL command and return any results

  Parameters:
  
  DB connection - pycobject
  SQL command   - string

  Returns:

  A list with one element per result set.
  Each element is a dictionary where the keys are column names
  and the values are lists containing the data for each column
  in the form of strings.
*/
static PyObject *_pybcp_exec_sql(PyObject *self, PyObject *args)
{
  PyObject *db_obj;
  char     *sql;
  db_connection *dbcon = NULL;
  RETCODE erc;
  struct COL
  {
    char *name;
    char *buffer;
    int type, size, status;
    PyObject *list;
  } *columns, *pcol;
  int ncols;
  int query_started;
  PyObject *result = NULL;

  columns = NULL;
  ncols   = 0;
  query_started = 0;

  /* Clear message buffers */
  last_msg[0] = 0;
  last_err[0] = 0;

  /* Get parameter values */
  if (!PyArg_ParseTuple(args, "Os", &db_obj, &sql))
    {
      SQL_EXCEPTION("Don't understand arguments!");
      goto cleanup;
    }

  /* Get pointer to DB connection struct */
  dbcon =  PTR_FROM_OBJECT(db_obj);
  
  /* Send command to server */
  RETCODE err = dbcmd(dbcon->dbproc, sql);
  if(err==FAIL)
    {
      SQL_EXCEPTION("Unable to send SQL command to server!\n");
      goto cleanup;
    }

  err = dbsqlexec(dbcon->dbproc);
  if(err==FAIL)
    {
      SQL_EXCEPTION("SQL command execution failed!")
      goto cleanup;
    }
  else
    {
      query_started = 1;
    }

  /*
    Process query results
  */
  result = PyList_New(0);
  while ((erc = dbresults(dbcon->dbproc)) != NO_MORE_RESULTS)
    {
      /* Add each result set as a dictionary in the results list */
      PyObject *dict = PyDict_New();
      PyList_Append(result, dict);
      Py_DECREF(dict);

      int row_code;
      if (erc == FAIL)
	{
	  SQL_EXCEPTION("dbresults call failed!");
	  goto cleanup;
	}

      ncols = dbnumcols(dbcon->dbproc);
      if ((columns = calloc(ncols, sizeof(struct COL))) == NULL)
	{
	  SQL_EXCEPTION("Unable to allocate memory!");
	  goto cleanup;
	}
      else
	{
	  for (pcol=columns; pcol - columns < ncols; pcol++)
	    pcol->buffer = NULL;
	}

      /*
       * Read metadata and bind.
       */
      for (pcol = columns; pcol - columns < ncols; pcol++)
	{
	  int c = pcol - columns + 1;

	  pcol->name = dbcolname(dbcon->dbproc, c);
	  pcol->type = dbcoltype(dbcon->dbproc, c);
	  pcol->size = 256; /* Fixed size string buffer */

	  /* Add each column as a dictionary entry */
	  pcol->list = PyList_New(0);
	  PyDict_SetItemString(dict, pcol->name, pcol->list);
	  Py_DECREF(pcol->list);
          
	  if ((pcol->buffer = calloc(1, pcol->size + 1)) == NULL)
	    {
	      SQL_EXCEPTION("Unable to allocate memory!");
	      goto cleanup;
	    }

	  erc = dbbind(dbcon->dbproc, c, NTBSTRINGBIND,
		       pcol->size+1, (BYTE*)pcol->buffer);
	  if (erc == FAIL)
	    {
	      SQL_EXCEPTION("dbbind call failed!");
	      goto cleanup;
	    }
			
	  erc = dbnullbind(dbcon->dbproc, c, &pcol->status);
	  if (erc == FAIL)
	    {
	      SQL_EXCEPTION("dbnullbind call failed!");
	      goto cleanup; 
	    }
	}

      /*
       * Append data to lists
       */
      while ((row_code = dbnextrow(dbcon->dbproc)) != NO_MORE_ROWS)
	{
	  switch (row_code)
	    {
	    case REG_ROW:
	      for (pcol=columns; pcol - columns < ncols; pcol++)
		{
		  char *buffer = pcol->status == -1 ? "NULL" : pcol->buffer;
		  //PyObject *str = PyString_FromString(buffer);
		  PyObject *str = PyUnicode_FromString(buffer);

		  PyList_Append(pcol->list, str);
		  Py_DECREF(str);
		}
	      break;
	    case BUF_FULL:
	      assert(row_code != BUF_FULL);
	      break;
	    case FAIL:
	      SQL_EXCEPTION("dbnextrow call failed!");
	      goto cleanup;
	    default:
		printf("Data for computeid %d ignored\n", row_code);
	    }
	}

      /* Free buffers */
      for (pcol=columns; pcol - columns < ncols; pcol++)
	{
	  free(pcol->buffer);
	  pcol->buffer = NULL;
	}
      free(columns);
      columns = NULL;

    }

  /* Done */
  return result;
  
 cleanup:
  if(result)Py_DECREF(result);
  if(query_started)dbcanquery(dbcon->dbproc);
  if(columns)
    {
      for (pcol=columns; pcol - columns < ncols; pcol++)
	if(pcol->buffer)free(pcol->buffer);
      free(columns);
    }
  return NULL;
}


/*
  Determine columns in the named table.

  Works by doing 'select top 0 * from table' and examining the
  columns of the (empty) result set.
*/
static PyObject *_pybcp_get_columns(PyObject *self, PyObject *args)
{
  PyObject *db_obj;
  char     *table;
  db_connection *dbcon = NULL;
  RETCODE erc;
  struct COL
  {
    char *name;
    char *buffer;
    int type, size, status;
  } *columns, *pcol;
  int ncols;
  int query_started;
  PyObject *result = NULL;
#define QUERY_LENGTH 1000
  char sql[QUERY_LENGTH];
  int num_results;

  columns = NULL;
  ncols   = 0;
  query_started = 0;

  /* Clear message buffers */
  last_msg[0] = 0;
  last_err[0] = 0;

  /* Get parameter values */
  if (!PyArg_ParseTuple(args, "Os", &db_obj, &table))
    {
      SQL_EXCEPTION("Don't understand arguments!");
      goto cleanup;
    }

  /* Get pointer to DB connection struct */
  dbcon = PTR_FROM_OBJECT(db_obj);
  
  /* Send command to server */
  snprintf(sql, QUERY_LENGTH, "select top 0 * from %s", table);
  RETCODE err = dbcmd(dbcon->dbproc, sql);
  if(err==FAIL)
    {
      SQL_EXCEPTION("Unable to send SQL command to server!\n");
      goto cleanup;
    }

  err = dbsqlexec(dbcon->dbproc);
  if(err==FAIL)
    {
      SQL_EXCEPTION("SQL command execution failed!")
      goto cleanup;
    }
  else
    {
      query_started = 1;
    }

  /*
    Will return a list with the column info
  */
  result = PyList_New(0);

  /*
    Process query results - should have exactly one result set
  */
  num_results = 0;
  while ((erc = dbresults(dbcon->dbproc)) != NO_MORE_RESULTS)
    {
      num_results += 1;
      if(num_results>1)
        {
	  SQL_EXCEPTION("Something wrong here - more than one result set getting columns!");
	  goto cleanup;
        }
        
      int row_code;
      if (erc == FAIL)
	{
	  SQL_EXCEPTION("dbresults call failed!");
	  goto cleanup;
	}

      ncols = dbnumcols(dbcon->dbproc);
      if ((columns = calloc(ncols, sizeof(struct COL))) == NULL)
	{
	  SQL_EXCEPTION("Unable to allocate memory!");
	  goto cleanup;
	}
      else
	{
	  for (pcol=columns; pcol - columns < ncols; pcol++)
	    pcol->buffer = NULL;
	}

      /*
       * Read metadata and bind.
       */
      for (pcol = columns; pcol - columns < ncols; pcol++)
	{
	  int c = pcol - columns + 1;

	  pcol->name = dbcolname(dbcon->dbproc, c);
	  pcol->type = dbcoltype(dbcon->dbproc, c);
	  pcol->size = dbcollen(dbcon->dbproc, c);
          
          /* Determine numpy type code for this column */
          int dtype;
          switch(pcol->type)
              {
              case(SYBINT4):
                  dtype = NPY_INT32;
                  break;
              case(SYBINT8):
                  dtype = NPY_INT64;
                  break;
              case(SYBREAL):
                  dtype = NPY_FLOAT32;
                  break;
              case(SYBFLT8):
                  dtype = NPY_FLOAT64;
                  break;
              case(SYBCHAR):
                  dtype = NPY_STRING;
                  break;
              default:
                  SQL_EXCEPTION("Unsupported data type!");
                  goto cleanup;
              }

          /* Create a numpy type descriptor for this column */
          PyArray_Descr *dtype_obj = PyArray_DescrNewFromType(dtype);
#if NPY_ABI_VERSION < 0x02000000
          dtype_obj->elsize = pcol->size;
#else
          PyDataType_SET_ELSIZE(dtype_obj, pcol->size);
#endif    
          /* Make (name, dtype) tuple for the column */
          PyObject *tuple = Py_BuildValue("sO", pcol->name, dtype_obj);
          Py_DECREF(dtype_obj);

          /* Append tuple to results */
          PyList_Append(result, tuple);
          Py_DECREF(tuple);

	  if ((pcol->buffer = calloc(1, pcol->size + 1)) == NULL)
	    {
	      SQL_EXCEPTION("Unable to allocate memory!");
	      goto cleanup;
	    }

	  erc = dbbind(dbcon->dbproc, c, NTBSTRINGBIND,
		       pcol->size+1, (BYTE*)pcol->buffer);
	  if (erc == FAIL)
	    {
	      SQL_EXCEPTION("dbbind call failed!");
	      goto cleanup;
	    }
			
	  erc = dbnullbind(dbcon->dbproc, c, &pcol->status);
	  if (erc == FAIL)
	    {
	      SQL_EXCEPTION("dbnullbind call failed!");
	      goto cleanup; 
	    }
	}

      /*
       * Iterate over all returned rows (should be none)
       */
      while ((row_code = dbnextrow(dbcon->dbproc)) != NO_MORE_ROWS)
	{
	  switch (row_code)
	    {
	    case REG_ROW:
              SQL_EXCEPTION("Something wrong here - call to get columns returned >0 results!");
	      goto cleanup;
	    case BUF_FULL:
	      assert(row_code != BUF_FULL);
	      break;
	    case FAIL:
	      SQL_EXCEPTION("dbnextrow call failed!");
	      goto cleanup;
	    default:
		printf("Data for computeid %d ignored\n", row_code);
	    }
	}

      /* Free buffers */
      for (pcol=columns; pcol - columns < ncols; pcol++)
	{
	  free(pcol->buffer);
	  pcol->buffer = NULL;
	}
      free(columns);
      columns = NULL;

    }
  if(num_results!=1)
    {
      SQL_EXCEPTION("Something wrong here - more than one result set getting columns!");
      goto cleanup;
    }

  /* Done */
  return result;
  
 cleanup:
  if(result)Py_DECREF(result);
  if(query_started)dbcanquery(dbcon->dbproc);
  if(columns)
    {
      for (pcol=columns; pcol - columns < ncols; pcol++)
	if(pcol->buffer)free(pcol->buffer);
      free(columns);
    }
  return NULL;
}


