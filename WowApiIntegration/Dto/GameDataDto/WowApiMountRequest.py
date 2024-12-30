from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMountRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    mountId = None

    def __init__(self, endpoint, mountId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.mountId = mountId
