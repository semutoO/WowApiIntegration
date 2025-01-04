from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest

class WowApiCharEquipSumRequest(AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
    def __init__(self, region, realmSlug, charName, namespace, locale, endpoint):
        super().__init__(region, namespace, locale, endpoint)
        self.realmSlug = realmSlug
        self.characterName = charName
