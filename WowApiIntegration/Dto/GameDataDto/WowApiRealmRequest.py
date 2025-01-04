from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiRealmRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, realmSlug = None, endpoint = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.realmSlug = realmSlug