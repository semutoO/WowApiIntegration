from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPowerTypeRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    powerTypeId = None

    def __init__(self, endpoint, powerTypeId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.powerTypeId = powerTypeId
