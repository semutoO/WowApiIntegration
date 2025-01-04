from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiMountRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, mountId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.mountId = mountId
