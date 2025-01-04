from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicRaidLeaderboardRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, raid = None, faction = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.raid = raid
        self.faction = faction
