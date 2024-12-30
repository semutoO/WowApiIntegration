from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicKeystoneDungeonLeaderboardRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    dungeonId = None
    periodId = None
    connectedRealmId = None

    def __init__(self, endpoint, dungeonId = None, periodId = None, connectedRealmId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.dungeonId = dungeonId
        self.periodId = periodId
        self.connectedRealmId = connectedRealmId
