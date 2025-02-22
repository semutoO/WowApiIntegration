from WowApiIntegration.Dto import AbstractWowApiRequest, AbstractWowApiSearchRequest

class WowApiItemRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, itemId = None, itemClassId = None, itemSetId = None, itemSubclassId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.itemId = itemId
        self.itemClassId = itemClassId
        self.itemSetId = itemSetId
        self.itemSubclassId = itemSubclassId

class WowApiItemSearchRequest(AbstractWowApiSearchRequest.AbstractWowApiSearchRequest):
    def __init__(self, orderBy="id", page=1, pageSize=50, endpoint=None, region=None, namespace="static-us", locale="en_US", searchDict:dict = None):
        super().__init__(orderBy, page, pageSize, endpoint, region, namespace, locale, searchDict)        