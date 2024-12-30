from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPlayableRaceRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    playableRaceId = None

    def __init__(self, endpoint, playableRaceId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.playableRaceId = playableRaceId
