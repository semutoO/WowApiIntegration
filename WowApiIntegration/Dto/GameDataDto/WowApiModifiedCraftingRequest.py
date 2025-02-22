from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiModifiedCraftingRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, categoryId = None, slotTypeId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.categoryId = categoryId
        self.slotTypeId = slotTypeId
