from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiItemRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, itemId = None, itemClassId = None, itemSetId = None, itemSubclassId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.itemId = itemId
        self.itemClassId = itemClassId
        self.itemSetId = itemSetId
        self.itemSubclassId = itemSubclassId
