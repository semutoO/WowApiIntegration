from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiReputationRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, reputationFactionId = None, reputationTierId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.reputationFactionId = reputationFactionId
        self.reputationTierId = reputationTierId