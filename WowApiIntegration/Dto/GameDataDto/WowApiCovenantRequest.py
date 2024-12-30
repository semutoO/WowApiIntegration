from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiCovenantRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    covenantId = None
    soulbindId = None    
    conduitId = None

    def __init__(self, endpoint, covenantId = None, soulbindId = None, conduitId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.covenantId = covenantId
        self.soulbindId = soulbindId
        self.conduitId = conduitId