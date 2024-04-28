#!/usr/bin/python3
"""Adds the State object “California”
with the City “San Francisco” to the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a new session
    session = Session(engine)

    # Create a new State object
    new_state = State(name='California')

    # Create a new City object
    new_city = City(name='San Francisco')

    # Append the new city to the cities relationship of the state
    new_state.cities.append(new_city)

    # Add the new state and city to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()

