from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPetRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    petId = None
    petAbilityId = None

    def __init__(self, endpoint, petId = None, petAbilityId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.petId = petId
        self.petAbilityId = petAbilityId
