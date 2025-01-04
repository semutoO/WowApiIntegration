from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest

class WowApiCharacterProfileRequest(AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):    
    def __init__(self, realmSlug, charName, namespace = None, locale = None, region = None, endpoint = None):
        super().__init__(realmSlug, charName, namespace)                
        self.region = region if region is not None else self.region
        self.locale = locale if locale is not None else self.locale
        self.endpoint = endpoint if endpoint is not None else self.endpoint