from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class GenericDAO:

    def __init__(self):	
        #engine = create_engine('sqlite:///database/britecore_db', echo=True)
        engine = create_engine('postgresql://postgres:password@localhost:5432', echo=True)
        self.Session = sessionmaker(bind=engine)

    def getSession(self):
        return self.Session()