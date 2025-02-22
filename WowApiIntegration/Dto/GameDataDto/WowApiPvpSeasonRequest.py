from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPvpSeasonRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, pvpSeasonId = None, pvpBracket = None, endpoint = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.pvpSeasonId = pvpSeasonId
        self.pvpBracket = pvpBracket
