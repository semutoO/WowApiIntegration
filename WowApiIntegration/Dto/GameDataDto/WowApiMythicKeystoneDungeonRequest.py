from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicKeystoneDungeonRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    dungeonId = None
    periodId = None
    seasonId = None

    def __init__(self, endpoint, dungeonId = None, periodId = None, seasonId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.dungeonId = dungeonId
        self.periodId = periodId
        self.seasonId = seasonId        
