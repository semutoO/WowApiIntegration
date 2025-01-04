from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicKeystoneDungeonLeaderboardRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, dungeonId = None, periodId = None, connectedRealmId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.dungeonId = dungeonId
        self.periodId = periodId
        self.connectedRealmId = connectedRealmId
