#!/usr/bin/python3

import MySQLdb
import sys

"""
a script that lists all states
from the database
"""
if __name__ == "__main__":
    param_args = sys.argv

    """connect to existing database"""

    link = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=param_args[1],
        password=param_args[2],
        database=param_args[3])

    """use the cursor to interact with the database"""
    cursor = link.cursor()

    """query the database for what you want in an order"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for eachstate in states:
        print(eachstate)

    """close the database and cursor"""

    cursor.close()
    link.close()
