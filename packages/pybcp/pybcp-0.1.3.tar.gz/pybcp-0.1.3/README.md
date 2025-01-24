# Python module for uploading numpy arrays to MS SQL Server

This module allows dictionaries of numpy arrays to be uploaded to SQL
Server as database tables. The upload is carried out as a bulk insert,
which copies binary data to the server without any conversion to or
from text. This is faster than uploading text and exactly preserves
floating point values.

## Compilation

The module uses [freetds](https://www.freetds.org/) to communicate
with the database server. To build the module, set the location of the
freetds library and headers and then run pip install. E.g.:
```
SYBDB=/cosma/local/freetds/1.4.20/ LDFLAGS="-L${SYBDB}/lib/ -Wl,-rpath=${SYBDB}/lib/" CFLAGS="-I${SYBDB}/include/" pip install .
```

## Usage

### Connect to the database:
```
dbcon = pybcp.DBConnection(username, server, database, password=None)
```
Here, `username` and `password` are the database username and password.
`server` is the server name defined in freetds.conf and `database` is
the name of the database which contains the table to be created or
updated.

If the password is None then a password prompt will appear.

### Uploading a database table

```
dbcon.bulk_insert(table_name, columns, create_table=True, drop_existing=True)
```
Here, `table_name` is the name of the table to create or append to. `columns`
is a dict of numpy arrays with the data for each column. If `create_table` is
true then a new table will be created. If `drop_existing` is true then any
existing table is removed first.

Table column arrays should be stored in an OrderedDict if the ordering
of the columns is important.

### Executing SQL commands

For convenience there's a function to execute SQL commands:
```
dbcon.execute(sql)
```
where `sql` is a string with the command to execute. This can be useful for
creating indexes on newly uploaded tables, for example.

This returns a list containing any tables returned by the command. Any
returned tables are represented as dictionaries of arrays in the same way
as data to be bulk inserted.