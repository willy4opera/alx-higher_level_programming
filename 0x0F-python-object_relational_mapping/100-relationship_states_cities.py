#!/usr/bin/python3

"""
Here, this script creates the State "California"
with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    dev_eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Base.metadata.create_all(dev_eng)

    Session = sessionmaker(bind=dev_eng)
    session = Session()

    n_state = State(name='California')
    n_city = City(name='San Francisco')
    n_state.cities.append(n_city)

    session.add(n_state)
    session.add(n_city)
    session.commit()
