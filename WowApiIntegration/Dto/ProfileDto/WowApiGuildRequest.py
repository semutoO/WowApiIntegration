from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest

class WowApiGuildRequest(AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):    
    def __init__(self, realmSlug, guildNameSlug, namespace = "profile-us", locale = "en_US", region = "us", endpoint = None):
        super().__init__(guildNameSlug, realmSlug, region, namespace, locale, endpoint)   