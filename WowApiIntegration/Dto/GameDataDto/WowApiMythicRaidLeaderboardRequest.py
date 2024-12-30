from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicRaidLeaderboardRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    raid = None
    faction = None

    def __init__(self, endpoint, raid = None, faction = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.raid = raid
        self.faction = faction
