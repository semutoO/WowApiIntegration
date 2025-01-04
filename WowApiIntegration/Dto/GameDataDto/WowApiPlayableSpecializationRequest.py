from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPlayableSpecializationRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, specId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.specId = specId
