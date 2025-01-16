from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest

class WowApiCharEquipSumRequest(AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
    def __init__(self, realmSlug, charName, namespace = "profile-us", locale = "en_US", region = "us", endpoint = None):
        super().__init__(charName, realmSlug, region, namespace, locale, endpoint)        