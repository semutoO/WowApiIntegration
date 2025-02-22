from WowApiIntegration.Dto import AbstractWowApiRequest


class AbstractWowApiProfileRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, characterName = None, realmSlug = None, namespace = "profile-us"):
        super().__init__(namespace=namespace if namespace is not None else "profile-us")
        self.characterName = characterName
        self.realmSlug = realmSlug        