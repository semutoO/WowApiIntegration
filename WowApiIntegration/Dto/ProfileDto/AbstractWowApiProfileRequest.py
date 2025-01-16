from WowApiIntegration.Dto import AbstractWowApiRequest


class AbstractWowApiProfileRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, characterName = None, realmSlug = None, region="us", namespace="profile-us", locale="en_US", endpoint = None):
        super().__init__(region=region, namespace=namespace if namespace is not None else "profile-us", locale=locale, endpoint=endpoint)
        self.characterName = characterName
        self.realmSlug = realmSlug        