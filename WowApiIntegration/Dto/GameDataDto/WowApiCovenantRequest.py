from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiCovenantRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, covenantId = None, soulbindId = None, conduitId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.covenantId = covenantId
        self.soulbindId = soulbindId
        self.conduitId = conduitId