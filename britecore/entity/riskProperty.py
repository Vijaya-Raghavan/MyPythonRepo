# riskProperty.py
from sqlalchemy import Column, String, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from britecore.entity.risk import Risk
from britecore.entity.propertyType import PropertyType

Base = declarative_base()

class RiskProperty(Base):

    __tablename__ = 'risk_prop'
    idSequence = Sequence('risk_prop_id_seq', metadata = Base.metadata)
    id = Column('id', Integer, idSequence, server_default = idSequence.next_value(), primary_key = True)
    riskId = Column('risk_id', Integer, ForeignKey(Risk.id), nullable=False)
    risk = relationship(Risk)
    propertyName = Column('prop_name', String, unique=True, nullable=False)
    propertyTypeId = Column('prop_type_id', Integer, ForeignKey(PropertyType.id), nullable=False)
    propertyType = relationship(PropertyType)
    propertyDescription = Column('prop_desc', String)
    propertyConstraint = Column('prop_constraint', String)
    propertyDefaultValue = Column('prop_default_val', String)

    def __init__(self, riskId, propertyName, propertyTypeId, propertyDescription, propertyConstraint, propertyDefaultValue):
        self.riskId = riskId
        self.propertyName = propertyName
        self.propertyTypeId = propertyTypeId
        self.propertyDescription = propertyDescription
        self.propertyConstraint = propertyConstraint
        self.propertyDefaultValue = propertyDefaultValue