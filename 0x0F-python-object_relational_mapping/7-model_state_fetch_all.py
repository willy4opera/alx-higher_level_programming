#!/usr/bin/python3

"""link class to table in database stated
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    dev_eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dev_eng)
    Session = sessionmaker(bind=dev_engi)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": "#!/usr/bin/python3

"""link class to table in database stated
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    dev_eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dev_eng)
    Session = sessionmaker(bind=dev_engi)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": "))
