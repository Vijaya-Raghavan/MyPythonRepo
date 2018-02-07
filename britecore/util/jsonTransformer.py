import jsonpickle
from britecore.view.riskProperty import RiskProperty
from britecore.view.propertyType import PropertyType

class JsonTransformer(object):

    def transformToJson(self, myObject):
        return jsonpickle.encode(myObject, unpicklable=False)

    def transformToObject(self, myJson):
        propertyName = myJson['propertyName']
        propertyTypeId = myJson['propertyType']['id']
        propertyTypeType = myJson['propertyType']['type']
        propertyDescription = myJson['propertyDescription']
        propertyConstraint = myJson['propertyConstraint']
        propertyDefaultValue = myJson['propertyDefaultValue']
        return RiskProperty(None, propertyName, PropertyType(propertyTypeId, propertyTypeType), propertyDescription, propertyConstraint, propertyDefaultValue)