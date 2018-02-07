# risk.py
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Risk(Base):

    __tablename__ = 'risk'
    idSequence = Sequence('risk_id_seq', metadata = Base.metadata)
    id = Column('id', Integer, idSequence, server_default = idSequence.next_value(), primary_key = True)
    name = Column('name', String, unique=True, nullable=False)

    def __init__(self, name):
        #self.id = id
        self.name = name