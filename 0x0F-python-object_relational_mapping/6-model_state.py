#!/usr/bin/python3

"""Here, we initiated the link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    dev_eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                            (sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Base.metadata.create_all(dev_eng)
