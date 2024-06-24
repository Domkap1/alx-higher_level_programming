#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb

def main():
    # User input (replace with actual values)
    mysql_user = "your_username"
    mysql_password = "your_password"
    db_name = "your_database"
    state_name = "California"  # Replace with the desired state name

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=mysql_user, passwd=mysql_password, db=db_name)
        cursor = db.cursor()

        # Create the SQL query using format
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            state_id, state_name = row
            print(f"State ID: {state_id}, Name: {state_name}")

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
