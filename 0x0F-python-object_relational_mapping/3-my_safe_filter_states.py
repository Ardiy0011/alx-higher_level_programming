#!/usr/bin/python3
"""
a script that lists all states
with names like that argument passed
"""
import MySQLdb
import sys


if __name__ == "__main__":
    param_args = sys.argv

    """connect to existing database"""
    if len(sys.argv) != 5:
        print("Invalid argument number")
        sys.exit(1)

    try:
        link = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=param_args[1],
            password=param_args[2],
            database=param_args[3])

        """user the cursor to interact with database"""
        cursor = link.cursor()

        """query database for what you want"""
        cursor.execute("SELECT *"
                       "FROM states WHERE name LIKE %s"
                       "ORDER BY id ASC", (param_args[4],))
        states = cursor.fetchall()
        for eachstate in states:
            print(eachstate)

    except MySQLdb.Error as error:
        print("Could not connect to server")

        """close database and cursor"""
        cursor.close()
        link.close()
