from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiRegionRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, regionId = None, endpoint = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.regionId = regionId