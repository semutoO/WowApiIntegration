from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiTalentRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, talentTreeId = None, specId = None, talentId = None, pvpTalentId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.talentTreeId = talentTreeId
        self.specId = specId
        self.talentId = talentId
        self.pvpTalentId = pvpTalentId