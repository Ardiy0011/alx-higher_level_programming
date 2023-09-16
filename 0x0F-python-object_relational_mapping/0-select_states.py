#!/usr/bin/python3
"""
a script that lists all states
from the database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    param_args = sys.argv

    """connect to existing database"""
    if len(sys.argv) != 4:
        print("Invalid argument number")
        sys.exit(1)

    try:
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

    except MySQLdb.Error as error:
        print("unable to connect to server")

        """close the database and cursor"""
    finally:
        cursor.close()
        link.close()
