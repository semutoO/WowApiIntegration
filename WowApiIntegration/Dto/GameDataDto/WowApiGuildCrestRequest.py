from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiGuildCrestRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, borderId = None, emblemId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.borderId = borderId
        self.emblemId = emblemId        