from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiCreatureRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, creatureId = None, creatureName = None, creatureDisplayId = None, creatureFamilyId = None, creatureTypeId = None, orderBy = "id", page = 1, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.creatureId = creatureId        
        self.creatureName = creatureName
        self.creatureDisplayId = creatureDisplayId
        self.creatureFamilyId = creatureFamilyId
        self.creatureTypeId = creatureTypeId
        self.orderBy = orderBy
        self._page = page
        