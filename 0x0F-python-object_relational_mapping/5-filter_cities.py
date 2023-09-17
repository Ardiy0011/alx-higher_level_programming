#!/usr/bin/python3
"""
a script that lists all cities with state
id equal to states id
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
        # Execute the SQL query to retrieve cities of the given state
        cursor.execute(
            "SELECT cities.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC",
            (param_args[4],)
        )

        # Fetch all the results
        cities = cursor.fetchall()

        result = ", ".join("".join(eachcity) for eachcity in cities)
        print(result)

    except MySQLdb.Error as error:
        print("MySQL Error:", error)
        sys.exit(1)

    finally:
        # Close the cursor and the database connection
        cursor.close()
        link.close()
