from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPowerTypeRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, powerTypeId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.powerTypeId = powerTypeId
