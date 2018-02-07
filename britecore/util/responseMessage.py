from britecore.view.message import Message

class ResponseMessage():

    def internalServerError(self):
        return Message('FAILURE', 'Internal Server Error')

    def riskCreated(self):
        return Message('SUCCESS', 'Risk with empty properties created.')

    def riskUpdated(self):
        return Message('SUCCESS', 'Risk updated.')

    def riskDeleted(self):
        return Message('SUCCESS', 'Risk with empty properties created.')

    def riskPropertyCreated(self):
        return Message('SUCCESS', 'Risk property created.')

    def riskPropertiesCreated(self):
        return Message('SUCCESS', 'Risk properties created.')

    def riskPropertyUpdated(self):
        return Message('SUCCESS', 'Risk property updated.')

    def riskPropertyDeleted(self):
        return Message('SUCCESS', 'Risk property deleted.')

    def riskPropertiesDeleted(self):
        return Message('SUCCESS', 'Risk properties deleted.')

    def riskExist(self):
        return Message('FAILURE', 'Risk(s) with same name already exist.')

    def riskNotExist(self):
        return Message('FAILURE', 'Unable to find risk(s).')

    def riskPropertyNotExist(self):
        return Message('FAILURE', 'Unable to find risk property(s).')

    def propertyTypeNotExist(self):
        return Message('FAILURE', 'Unable to find property type(s).')
