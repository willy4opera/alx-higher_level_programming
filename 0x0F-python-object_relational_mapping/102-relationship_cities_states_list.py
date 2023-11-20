#!/usr/bin/python3

"""Here, this script prints the State
object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    dev_eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dev_eng)
    Session = sessionmaker(bind=dev_eng)
    session = Session()
    for insta in session.query(State).order_by(State.id):
        for city_i in insta.cities:
            print(city_i.id, city_i.name, sep=": ", end="")
            print(" -> " + insta.name)
