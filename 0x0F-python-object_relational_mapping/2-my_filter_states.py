#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the states
    from the database.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    db_cursor.execute(query, (argv[4],))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
