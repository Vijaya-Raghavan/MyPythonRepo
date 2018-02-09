import sys
import traceback
from britecore.dao.propertyTypeDao import PropertyTypeDAO
from britecore.dao.riskDao import RiskDAO
from britecore.dao.riskPropertyDao import RiskPropertyDAO
from britecore.view.propertyType import PropertyType
from britecore.view.risk import Risk
from britecore.view.riskProperty import RiskProperty
from britecore.entity.riskProperty import RiskProperty as RiskPropertyEntity
from britecore.util.responseMessage import ResponseMessage

class BriteCoreService():

    def __init__(self):
        self.propertyTypeDao = PropertyTypeDAO()
        self.riskDao = RiskDAO()
        self.riskPropertyDao = RiskPropertyDAO()
        self.responseMessage = ResponseMessage()

    def getAllPropertyTypes(self):
        propertyTypes = []
        message = None
        try:
            propertyTypeEntities = self.propertyTypeDao.getAllPropertyTypes()
            if propertyTypeEntities is not None and propertyTypeEntities.__len__() > 0:
                for propertyTypeEntity in propertyTypeEntities:
                    propertyTypes.append(PropertyType(propertyTypeEntity.id, propertyTypeEntity.type))
            else:
                message = self.responseMessage.propertyTypeNotExist()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        if message is not None:
            return message
        else:
            return propertyTypes
    
    def getAllRisks(self):
        risks = []
        message = None
        try:
            riskEntities = self.riskDao.getAllRisks()
            if riskEntities is not None and riskEntities.__len__() > 0:
                for riskEntity in riskEntities:
                    risks.append(Risk(riskEntity.id, riskEntity.name))
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        if message is not None:
            return message
        else:
            return risks

    def getRiskProperties(self, riskId):
        riskProperties = []
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                riskPropertyEntities = self.riskPropertyDao.getRiskProperties(riskId)
                if riskPropertyEntities is not None and riskPropertyEntities.__len__() > 0:
                    for riskPropertyEntity in riskPropertyEntities:
                        propertyTypeEntity = self.propertyTypeDao.findPropertyType(riskPropertyEntity.propertyTypeId)
                        riskProperties.append(RiskProperty(riskPropertyEntity.id, riskPropertyEntity.propertyName, PropertyType(propertyTypeEntity.id, propertyTypeEntity.type), riskPropertyEntity.propertyDescription, riskPropertyEntity.propertyConstraint, riskPropertyEntity.propertyDefaultValue))
                else:
                    message = self.responseMessage.riskPropertyNotExist()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        if message is not None:
            return message
        else:
            return riskProperties

    def findRisk(self, riskId):
        risk = None
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                risk = Risk(riskEntity.id, riskEntity.type)
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        if message is not None:
            return message
        else:
            return risk

    def findRisks(self, riskName):
        risks = []
        message = None
        try:
            riskEntities = self.riskDao.findRisks(riskName)
            if riskEntities is not None and riskEntities.__len__() > 0:
                for riskEntity in riskEntities:
                    risks.append(Risk(riskEntity.id, riskEntity.type))
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        if message is not None:
            return message
        else:
            return risks

    def addRisk(self, riskName):
        message = None
        try:
            riskEntities = self.riskDao.findRiskWithExactMatch(riskName)
            if riskEntities is None or riskEntities.__len__() == 0:
                self.riskDao.addRisk(riskName)
                message = self.responseMessage.riskCreated()
            else:
                message = self.responseMessage.riskExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def updateRisk(self, riskId, riskName):
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                self.riskDao.updateRisk(riskId, riskName)
                message = self.responseMessage.riskUpdated()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def deleteRisk(self, riskId):
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                self.riskPropertyDao.deleteAllRiskProperties(riskId)
                self.riskDao.deleteRisk(riskId)
                message = self.responseMessage.riskDeleted()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def addRiskProperty(self, riskId, riskProperty):
        message = None
        try:
            riskEntity = self.findRisk(riskId)
            if riskEntity is not None:
                propertyTypeEntity = self.propertyTypeDao.findPropertyType(riskProperty.propertyType.id)
                if propertyTypeEntity is not None:
                    riskPropertyEntity = RiskPropertyEntity(riskId, riskProperty.propertyName, riskProperty.propertyType.id, riskProperty.propertyDescription, riskProperty.propertyConstraint, riskProperty.propertyDefaultValue)
                    self.riskPropertyDao.addRiskProperty(riskPropertyEntity)
                    message = self.responseMessage.riskPropertyCreated()
                else:
                    message = self.responseMessage.propertyTypeNotExist()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def addRiskProperties(self, riskId, riskProperties):
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                riskPropertyEntities = []
                for riskProperty in riskProperties:
                    propertyTypeEntity = self.propertyTypeDao.findPropertyType(riskProperty.propertyType.id)
                    if propertyTypeEntity is not None:
                        riskPropertyEntities.append(RiskPropertyEntity(riskId, riskProperty.propertyName, riskProperty.propertyType.id, riskProperty.propertyDescription, riskProperty.propertyConstraint, riskProperty.propertyDefaultValue))
                    else:
                        message = self.responseMessage.propertyTypeNotExist()
                if riskPropertyEntities.__len__() > 0:
                    self.riskPropertyDao.addRiskProperties(riskPropertyEntities)
                    message = self.responseMessage.riskPropertiesCreated()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def updateRiskProperty(self, riskId, riskPropertyId, riskProperty):
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                riskPropertyEntity = self.riskPropertyDao.findRiskProperty(riskId, riskPropertyId)
                if riskPropertyEntity is not None:
                    propertyTypeEntity = self.propertyTypeDao.findPropertyType(riskProperty.propertyType.id)
                    if propertyTypeEntity is not None:
                        riskPropertyEntity.propertyName = riskProperty.propertyName
                        riskPropertyEntity.propertyTypeId = propertyTypeEntity.id
                        riskPropertyEntity.propertyDescription = riskProperty.propertyDescription
                        riskPropertyEntity.propertyConstraint = riskProperty.propertyConstraint
                        riskPropertyEntity.propertyDefaultValue = riskProperty.propertyDefaultValue
                        self.riskPropertyDao.updateRiskProperty(riskId, riskPropertyId, riskPropertyEntity)
                        message = self.responseMessage.riskPropertyUpdated()
                    else:
                        message = self.responseMessage.propertyTypeNotExist()
                else:
                    message = self.responseMessage.riskPropertyNotExist()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def deleteRiskProperty(self, riskId, riskPropertyId):
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                riskPropertyEntity = self.riskPropertyDao.findRiskProperty(riskId, riskPropertyId)
                if riskPropertyEntity is not None:
                    self.riskPropertyDao.deleteRiskProperty(riskId, riskPropertyId)
                    message = self.responseMessage.riskPropertyDeleted()
                else:
                    message = self.responseMessage.riskPropertyNotExist()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;

    def deleteRiskProperties(self, riskId):
        message = None
        try:
            riskEntity = self.riskDao.findRisk(riskId)
            if riskEntity is not None:
                self.riskPropertyDao.deleteRiskProperties(riskId)
                message = self.responseMessage.riskPropertiesDeleted()
            else:
                message = self.responseMessage.riskNotExist()
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            message = self.responseMessage.internalServerError()
        return message;
