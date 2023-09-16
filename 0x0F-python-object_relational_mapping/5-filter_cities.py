#!/usr/bin/python3


import MySQLdb
import sys

"""
a script that lists all cities with state
id equal to states id
"""
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
        cursor.execute(
            "SELECT cities.name "
            "FROM cities "
            "INNER JOIN state ON cities.state_id = {}.id "
            "ORDER BY id ASC"
            .format(param_args[4]))

        states = cursor.fetchall()
        for eachstate in states:
            print(eachstate)

    except MySQLdb.Error as error:
        print("Could not connect to server")

        """close database and cursor"""
        cursor.close()
        link.close()
