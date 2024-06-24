#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb

def filter_states(username, password, database, state_name):
  """
  Filters states table based on a provided state name.

  Args:
    username: MySQL username.
    password: MySQL password.
    database: Database name.
    state_name: State name to search for.
  """
  try:
    # Connect to MySQL server
    connection = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cursor = connection.cursor()

    # Prepare SQL query with user input
    query = """
      SELECT *
      FROM states
      WHERE name = '{}'
      ORDER BY states.id ASC
    """.format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch results
    results = cursor.fetchall()
`
    # Check for results
    if not results:
      print("No state found")
    else:
      # Print results formatted as requested
      for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")

  except MySQLdb.Error as err:
    print(f"Error connecting to database: {err}")
  finally:
    # Close connection
    if connection:
      connection.close()

if __name__ == "__main__":
  # Script execution is disabled when imported
  pass
