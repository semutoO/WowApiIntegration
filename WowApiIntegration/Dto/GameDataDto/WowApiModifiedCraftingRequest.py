from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiModifiedCraftingRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    categoryId = None
    slotTypeId = None

    def __init__(self, endpoint, categoryId = None, slotTypeId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.categoryId = categoryId
        self.slotTypeId = slotTypeId
