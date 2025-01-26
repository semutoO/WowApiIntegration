from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiAccountProfileRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, realmId, characterId, namespace = "profile-us", locale = "en_US", region = "us", endpoint = None):
        super().__init__(region, namespace, locale, endpoint)   
        self.realmId = realmId
        self.characterId = characterId