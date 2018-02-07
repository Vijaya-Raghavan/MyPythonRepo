# propertyType.py
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PropertyType(Base):

    __tablename__ = 'prop_type'
    idSequence = Sequence('prop_type_id_seq', metadata = Base.metadata)
    id = Column('id', Integer, idSequence, server_default = idSequence.next_value(), primary_key = True)
    type = Column('type', String, unique = True, nullable = False)

    def __init__(self, type):
        #self.id = id
        self.type = type
