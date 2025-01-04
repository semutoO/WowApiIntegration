from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPlayableRaceRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, playableRaceId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.playableRaceId = playableRaceId
