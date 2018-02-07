from britecore.dao.genericDao import GenericDAO
from britecore.entity.riskProperty import RiskProperty

class RiskPropertyDAO(GenericDAO):

    def getRiskProperties(self, riskId):
        riskPropertyEntities = None
        session = self.getSession()
        try:
            riskPropertyEntities = session.query(RiskProperty).filter(RiskProperty.riskId == riskId).order_by(RiskProperty.id).all()       
        except:
            raise
        finally:
            session.close()
        return riskPropertyEntities

    def findRiskProperty(self, riskPropertyId):
        riskPropertyEntity = None
        session = self.getSession()
        try:
            riskPropertyEntity = session.query(RiskProperty).filter(RiskProperty.id == riskPropertyId).first()
        except:
            raise
        finally:
            session.close()
        return riskPropertyEntity

    def findRiskProperty(self, riskId, riskPropertyId):
        riskPropertyEntity = None
        session = self.getSession()
        try:
            riskPropertyEntity = session.query(RiskProperty).filter(RiskProperty.riskId == riskId).filter(RiskProperty.id == riskPropertyId)
        except:
            raise
        finally:
            session.close()
        return riskPropertyEntity

    def addRiskProperty(self, riskProperty):
        session = self.getSession()
        try:
            session.add(riskProperty)
            session.commit()
        except:
            raise
        finally:
            session.close()

    def addRiskProperties(self, riskProperties):
        session = self.getSession()
        try:
            session.bulk_save_objects(riskProperties)
            session.commit()
        except:
            raise
        finally:
            session.close()

    def updateRiskProperty(self, riskId, riskPropertyId, riskProperty):
        session = self.getSession()
        try:
            session.query(RiskProperty).filter(RiskProperty.id == riskPropertyId).filter(RiskProperty.riskId == riskId).update({RiskProperty.propertyName : riskProperty.propertyName, RiskProperty.propertyTypeId : riskProperty.propertyTypeId, RiskProperty.propertyDescription : riskProperty.propertyDescription, RiskProperty.propertyConstraint : riskProperty.propertyConstraint, RiskProperty.propertyDefaultValue : riskProperty.propertyDefaultValue})
            session.commit()
        except:
            raise
        finally:
            session.close()

    def deleteRiskProperty(self, riskId, riskPropertyId):
        session = self.getSession()
        try:
            session.query(RiskProperty).filter(RiskProperty.id == riskPropertyId).filter(RiskProperty.riskId == riskId).delete()
            session.commit()
        except:
            raise
        finally:
            session.close()

    def deleteRiskProperties(self, riskId):
        session = self.getSession()
        try:
            session.query(RiskProperty).filter(RiskProperty.riskId == riskId).delete()
            session.commit()
        except:
            raise
        finally:
            session.close()

    def getSession(self):
        return super(RiskPropertyDAO, self).getSession()