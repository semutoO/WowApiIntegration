from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMythicKeystoneAffixRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    keystoneAffixId = None

    def __init__(self, endpoint, keystoneAffixId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.keystoneAffixId = keystoneAffixId
