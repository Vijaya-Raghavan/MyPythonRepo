from flask import Flask, request, Response
from flask_accept import accept
from britecore.service.briteCoreService import BriteCoreService
from britecore.util.jsonTransformer import JsonTransformer
from britecore.util.briteCoreUtil import BriteCoreUtil

app = Flask(__name__)
briteCoreService = BriteCoreService()
jTransformer = JsonTransformer()
briteCoreUtil = BriteCoreUtil()

@app.route('/propertyType/all', methods = ['GET'])
def getAllPropertyTypes():
    resp = briteCoreService.getAllPropertyTypes()
    return briteCoreUtil.getResponse(resp)

@app.route('/propertyType/add/<string:propertyType>', methods = ['GET'])
def addPropertyType(propertyType):
    resp = briteCoreService.addPropertyType(propertyType)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/all', methods = ['GET'])
def getAllRisks():
    resp = briteCoreService.getAllRisks()
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>/properties', methods = ['GET'])
def getRiskProperties(riskId):
    resp = briteCoreService.getRiskProperties(riskId)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>', methods = ['GET'])
def findRisk(riskId):
    resp = briteCoreService.findRisk(riskId)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<string:riskName>', methods = ['GET'])
def findRisks(riskName):
    resp = briteCoreService.findRisks(riskName)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/add', methods = ['POST'])
@accept('application/json')
def addRisk():
    data = request.get_json()
    name = data['name']
    resp = briteCoreService.addRisk(name)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>/addRiskProperty', methods = ['POST'])
@accept('application/json')
def addRiskProperty(riskId):
    data = request.get_json()
    riskProperty = jTransformer.transformToObject(data)
    resp = briteCoreService.addRiskProperty(riskId, riskProperty)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>/addRiskProperties', methods = ['POST'])
@accept('application/json')
def addRiskProperties(riskId):
    data = request.get_json()
    riskProperties = jTransformer.transformToObject(data)
    resp = briteCoreService.addRiskProperties(riskId, riskProperties)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>/updateRiskProperty/<int:propertyId>', methods = ['PUT'])
@accept('application/json')
def updateRiskProperty(riskId, propertyId):
    data = request.get_json()
    riskProperty = jTransformer.transformToObject(data)
    resp = briteCoreService.updateRiskProperty(riskId, propertyId, riskProperty)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>/deleteRiskProperty/<int:propertyId>', methods = ['DELETE'])
def deleteRiskProperty(riskId, propertyId):
    resp = briteCoreService.deleteRiskProperty(riskId, propertyId)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/<int:riskId>/deleteRiskProperties', methods = ['DELETE'])
def deleteRiskProperties(riskId):
    resp = briteCoreService.deleteRiskProperties(riskId)
    return briteCoreUtil.getResponse(resp)

@app.route('/risk/delete/<int:riskId>', methods = ['DELETE'])
def deleteRisk(riskId):
    resp = briteCoreService.deleteRisk(riskId)
    return briteCoreUtil.getResponse(resp)

if __name__ == '__main__':
    app.run()