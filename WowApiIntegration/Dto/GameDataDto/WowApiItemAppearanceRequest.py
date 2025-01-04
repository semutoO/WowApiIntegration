from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiItemAppearanceRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, appearanceId = None, appearanceSetId = None, slotType = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.appearanceId = appearanceId
        self.appearanceSetId = appearanceSetId
        self.slotType = slotType