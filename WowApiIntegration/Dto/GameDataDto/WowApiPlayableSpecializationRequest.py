from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPlayableSpecializationRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    specId = None

    def __init__(self, endpoint, specId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.specId = specId
