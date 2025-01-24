#!/bin/env python

import numpy as np
import _pybcp
from getpass import getpass
from collections import OrderedDict
import re
from multiprocessing import Process

SQLError = _pybcp.SQLError

def sql_type(dtype):
    """
    Given a numpy data type, return the corresponding SQL type
    """
    if dtype.kind in ("i","u","f"):
        # It's a numeric type
        if dtype == np.int32:
            return "integer"
        elif dtype == np.int64:
            return "bigint"
        elif dtype == np.float32:
            return "real"
        elif dtype == np.float64:
            return "float"
        else:
            raise ValueError("Unsupported data type "+str(dtype))
    elif dtype.kind == "S":
        # It's a string
        # Note: this assumes 1 byte = 1 character!
        return ("char(%d)" % dtype.itemsize)
    else:
        # Not numeric or string, don't know what to do with this!
        raise ValueError("Unsupported data type "+str(dtype))   


def numpy_type(sqltype):
    """
    Given an SQL data type, return the corresponding numpy type
    """
    m = re.match("char\(([0-9]+)\)", sqltype.strip())
    if m is not None:
        # It's a string
        return np.dtype("|S"+m.group(1))
    else:
        # It's a numeric type
        if sqltype == "integer" or sqltype == "int":
            return np.int32
        elif sqltype == "bigint":
            return np.int64
        elif sqltype == "real":
            return np.float32
        elif sqltype == "float":
            return np.float64
        else:
            raise ValueError("Unsupported data type "+sqltype)

class DBConnection:  

    """
    Class allowing a connection to a database using FreeTDS
    """
    def __init__(self, username, database, context, password=None):
        if password is None:
            password = getpass("Enter database password:")
        self.dbparams = (username, password, database, context)
        self._open()

    def _open(self):
        """Open a connection to the database"""
        (username, password, database, context) = self.dbparams
        self.dbcon = _pybcp.connect(username, password, database, context)

    def _close(self):
        """Close the database connection"""
        self.dbcon = None

    def execute(self, sql):
        """Execute an SQL command and return the result"""
        return _pybcp.exec_sql(self.dbcon, sql)

    def create_table(self, table, columns, drop_existing=False):
        """Create a table using the specified column names and numpy data types"""
        if drop_existing:
            try:
                self.execute("drop table "+table)
            except _pybcp.SQLError:
                pass
        sql = "create table " + table + " ("
        for name, dtype in columns.items():
            sql += "[" + name + "] " + sql_type(dtype) + " not null,"
        sql = sql[:-1] + ");"
        self.execute(sql)

    def drop_table(self, table):
        """Drop the specified table"""
        sql = "drop table "+table
        self.execute(sql)

    def get_columns(self, table):
        """Return names and numpy types for table columns"""
        return _pybcp.get_columns(self.dbcon, table)

    def bulk_insert(self, table, data, create_table=False, drop_existing=False, 
                    callback=None, ncallback=100000):
        """Bulk insert a dictionary of numpy arrays as table columns"""
        # Open database connection if necessary
        if self.dbcon is None:
            self._open()
        # Create the table if requested
        if create_table:
            cols = OrderedDict()
            for name, arr in data.items():
                cols[name] = arr.dtype
            self.create_table(table, cols, drop_existing)
        # Flag which of the supplied data arrays we're importing
        dataflag = {}
        for name in data.keys():
            dataflag[name] = False
        # Loop over existing columns in the table
        import_cols = []
        for col_name, col_type in self.get_columns(table):
            # Find the data for this column and check it's the right type
            if col_name not in data:
                raise SQLError("Data not found for column "+col_name)
            if col_type.kind=="S":
                # Strings column, so just check both are strings
                if data[col_name].dtype.kind != "S":
                    raise SQLError("Data has wrong type for column "+col_name)
            else:
                # Numeric types should match exactly
                if data[col_name].dtype != col_type:
                    raise SQLError("Data has wrong type for column "+col_name)
            # Add to the list of arrays to import
            import_cols.append(data[col_name])
            dataflag[col_name] = True
        # Check we're importing all the supplied data
        if not(all(dataflag.values())):
            raise SQLError("Not all data arrays correspond to table columns!")
        # Bulk insert the data
        _pybcp.bulk_insert(self.dbcon, table, import_cols, callback, ncallback)


class AsyncDBConnection (DBConnection):  
    """
    Database connection class that runs the bulk insert in a separate process
    """
    def __init__(self, username, database, context, password=None):
        DBConnection.__init__(self, username, database, context, password)
        self.import_process = None

    def bulk_insert(self, table, data, create_table=False, drop_existing=False, 
                    callback=None, ncallback=100000):
        # Wait until any already running import finishes
        if self.import_process is not None:
            self.import_process.join()
            self.import_process = None
        # Close database connection
        self._close()
        # Run the import in a new process
        self.import_process = Process(target=DBConnection.bulk_insert,
                                      args=(self, table, data, create_table, drop_existing, None, 0))
        self.import_process.start()
        # Re-open database connection
        self._open()

    def wait(self):
        """Wait for any running process to finish"""
        if self.import_process is not None:
            self.import_process.join()
            self.import_process = None
