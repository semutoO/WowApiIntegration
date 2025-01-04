from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiTechTalentRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, techTalentTreeId = None, techTalentId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.techTalentTreeId = techTalentTreeId
        self.techTalentId = techTalentId