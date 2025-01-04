from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicKeystoneAffixRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, keystoneAffixId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.keystoneAffixId = keystoneAffixId
