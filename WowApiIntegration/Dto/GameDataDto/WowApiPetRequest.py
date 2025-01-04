from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPetRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, petId = None, petAbilityId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.petId = petId
        self.petAbilityId = petAbilityId
