#!/bin/env python
#
# Script to import data from a text file into
# a database table
#

import numpy as np
import pybcp

filename   = "redshift_list.txt"
table_name = "test_table"

# Make data type corresponding to one row
row_t = np.dtype([
        ("snapnum",  np.int32),
        ("redshift", np.float64),
        ])

# Read in the data from the text file
data = np.loadtxt(filename, dtype=row_t)

# Connect to database
username = "jch"
database = "Eagle_private"
dbcon = pybcp.DBConnection(username, "virgodb2", database, 
                           password=None) # will prompt for password

# Make dictionary of arrays with table column data
columns = {}
for name in row_t.fields:
    columns[name] = data[name]

# Import the data
dbcon.bulk_insert(table_name, columns, create_table=True, drop_existing=True)

print "Done."
