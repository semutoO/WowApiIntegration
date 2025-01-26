from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest

class WowApiCharacterPvpRequest(AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):    
    def __init__(self, realmSlug, characterName, pvpBracket, namespace = "profile-us", locale = "en_US", region = "us", endpoint = None):
        super().__init__(characterName, realmSlug, region, namespace, locale, endpoint)   
        self.pvpBracket = pvpBracket