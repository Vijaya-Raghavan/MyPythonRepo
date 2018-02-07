from britecore.dao.genericDao import GenericDAO
from britecore.entity.propertyType import PropertyType

class PropertyTypeDAO(GenericDAO):

    def getAllPropertyTypes(self):
        propertyTypeEntities = None
        session = self.getSession()
        try:
            propertyTypeEntities = session.query(PropertyType).order_by(PropertyType.id).all()
        except:
            raise
        finally:
            session.close()
        return propertyTypeEntities

    def addPropertyType(self, propertyType):
        session = self.getSession()
        try:
            session.add(PropertyType(propertyType))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def findPropertyType(self, propertyTypeId):
        propertyTypeEntity = None
        session = self.getSession()
        try:
            propertyTypeEntity = session.query(PropertyType).filter(PropertyType.id == propertyTypeId).first()
        except:
            raise
        finally:
            session.close()
        return propertyTypeEntity

    def getSession(self):
        return super(PropertyTypeDAO, self).getSession()