from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiToyRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, toyId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.toyId = toyId