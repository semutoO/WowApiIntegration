from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiCharacterProfileRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    realmSlug = None
    characterName = None
    endpoint = None

    def __init__(self, region, realmSlug, charName, namespace, locale, endpoint):
        self.region = region
        self.realmSlug = realmSlug
        self.characterName = charName
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
