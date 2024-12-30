from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiItemAppearanceRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    appearanceId = None
    appearanceSetId = None
    slotType = None

    def __init__(self, endpoint, appearanceId = None, appearanceSetId = None, slotType = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.appearanceId = appearanceId
        self.appearanceSetId = appearanceSetId
        self.slotType = slotType