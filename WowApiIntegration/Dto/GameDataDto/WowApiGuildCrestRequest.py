from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiGuildCrestRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    borderId = None
    emblemId = None        

    def __init__(self, endpoint, borderId = None, emblemId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.borderId = borderId
        self.emblemId = emblemId        