from WowApiIntegration.Dto import AbstractWowApiRequest, AbstractWowApiSearchRequest


class WowApiConnectedRealmRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, connectedRealmId = None, endpoint = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)        
        self.connectedRealmId = connectedRealmId        

class WowApiConnectedRealmSearchRequest(AbstractWowApiSearchRequest.AbstractWowApiSearchRequest):
    def __init__(self, orderBy = None, page = 1, pageSize = 50, endpoint = None, region=None, namespace="dynamic-us", locale=None, searchDict:dict = None):
        super().__init__(orderBy, page, pageSize, endpoint, region, namespace, locale, searchDict)