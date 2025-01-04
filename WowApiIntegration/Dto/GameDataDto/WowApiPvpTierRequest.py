from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPvpTierRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, pvpTierId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.pvpTierId = pvpTierId