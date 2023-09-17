#!/usr/bin/python3
"""
A script to connect to a MySQL database and list states.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import create_engine


if __name__ == "__main__":
    param_args = sys.argv
    """Check for the correct number of command-line arguments"""
    if len(param_args) != 5:
        print("low no. of arguments")
        sys.exit(1)

    """Extract command-line arguments"""

    u_name = param_args[1]
    p_wd = param_args[2]
    db = param_args[3]

    """Create a database engine with proper URL formatting"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(u_name, p_wd, db), pool_pre_ping=True)

    """Create tables if they don't exist"""
    Base.metadata.create_all(engine)

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Retrieve and display1st state object with name of argument"""
    first_state = session.query(
        State).filter(State.name == param_args[4]).first()
    if first_state:
        print("{}".format(first_state.id))
    else:
        print("Not found")

    """Close the session"""
    session.close()
