from britecore.dao.genericDao import GenericDAO
from britecore.entity.risk import Risk

class RiskDAO(GenericDAO):

    def getAllRisks(self):
        riskEntities = None
        session = self.getSession()
        try:
            riskEntities = session.query(Risk).order_by(Risk.id).all()
        except:
            raise
        finally:
            session.close()
        return riskEntities

    def findRisk(self, riskId):
        riskEntity = None
        session = self.getSession()
        try:
            riskEntity = session.query(Risk).filter(Risk.id == riskId).first()
        except:
            raise
        finally:
            session.close()
        return riskEntity

    def findRisks(self, riskName):
        riskEntities = None
        session = self.getSession()
        try:
            riskEntities = session.query(Risk).filter(Risk.name.like('%' + riskName + '%')).order_by(Risk.id).all()
        except:
            raise
        finally:
            session.close()
        return riskEntities

    def findRiskWithExactMatch(self, riskName):
        riskEntities = None
        session = self.getSession()
        try:
            riskEntities = session.query(Risk).filter(Risk.name == riskName).order_by(Risk.id).all()
        except:
            raise
        finally:
            session.close()
        return riskEntities
    
    def addRisk(self, riskName):
        session = self.getSession()
        try:
            session.add(Risk(riskName))
            session.commit()
        except:
            raise
        finally:
            session.close()

    def updateRisk(self, riskId, riskName):
        session = self.getSession()
        try:
            session.query(Risk).filter(Risk.id == riskId).update({Risk.name : riskName})
            session.commit()
        except:
            raise
        finally:
            session.close()

    def deleteRisk(self, riskId, riskName):
        session = self.getSession()
        try:
            session.query(Risk).filter(Risk.id == riskId).delete()
            session.commit()
        except:
            raise
        finally:
            session.close()

    def getSession(self):
        return super(RiskDAO, self).getSession()