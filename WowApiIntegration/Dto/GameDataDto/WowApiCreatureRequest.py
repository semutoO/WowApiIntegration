from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiCreatureRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    creatureId = None
    creatureName = None
    creatureDisplayId = None
    creatureFamilyId = None
    creatureTypeId = None
    orderBy = "id"
    _page = 1

    def __init__(self, endpoint, creatureId = None, creatureName = None, creatureDisplayId = None, creatureFamilyId = None, creatureTypeId = None, orderBy = "id", page = 1, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.creatureId = creatureId        
        self.creatureName = creatureName
        self.creatureDisplayId = creatureDisplayId
        self.creatureFamilyId = creatureFamilyId
        self.creatureTypeId = creatureTypeId
        self.orderBy = orderBy
        self._page = page
        