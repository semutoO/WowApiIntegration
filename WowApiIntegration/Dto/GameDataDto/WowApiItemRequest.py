from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiItemRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    itemId = None
    itemClassId = None
    itemSetId = None
    itemSubclassId = None

    def __init__(self, endpoint, itemId = None, itemClassId = None, itemSetId = None, itemSubclassId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.itemId = itemId
        self.itemClassId = itemClassId
        self.itemSetId = itemSetId
        self.itemSubclassId = itemSubclassId
