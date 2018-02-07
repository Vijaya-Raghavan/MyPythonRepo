from flask import Response
from britecore.util.jsonTransformer import JsonTransformer
from britecore.util.responseMessage import ResponseMessage
from britecore.view.message import Message

class BriteCoreUtil:

    def __init__(self):
        self.jTransformer = JsonTransformer()

    def getStatus(self, resp):
        status = 200
        if isinstance(resp, Message):
            if resp.status == 'FAILURE':
                status = 400
                if resp.text == 'Internal Server Error':
                    status = 500
        return status

    def getResponse(self, resp):
        responseStatus = self.getStatus(resp)
        jsonResponse = self.jTransformer.transformToJson(resp)
        response = Response(jsonResponse, status=responseStatus, mimetype='application/json')
        return response
        
