from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiTitleRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, titleId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.titleId = titleId