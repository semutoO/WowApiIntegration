from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicKeystoneDungeonRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, dungeonId = None, periodId = None, seasonId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.dungeonId = dungeonId
        self.periodId = periodId
        self.seasonId = seasonId        
