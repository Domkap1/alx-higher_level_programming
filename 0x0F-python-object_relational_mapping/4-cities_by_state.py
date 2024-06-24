#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the database
    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    # Create query to fetch cities with state information and sorted by cities.id
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    # Execute the query
    db_cursor.execute(query)

    # Fetch all rows
    rows_selected = db_cursor.fetchall()

    # Print each row as specified
    for row in rows_selected:
        print(row)

    # Close cursor and connection
    db_cursor.close()
    db_connect.close()

