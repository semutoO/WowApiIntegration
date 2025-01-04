from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiProfessionRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, professionId = None, skillTierId = None, recipeId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.professionId = professionId
        self.skillTierId = skillTierId
        self.recipeId = recipeId
