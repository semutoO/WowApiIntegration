from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiConnectedRealmRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, status = None, realmTimeZone = "America/New_York", orderBy = "id", page = 1, connectedRealmId = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)        
        self.connectedRealmId = connectedRealmId
        self.status = status
        self.realmTimeZone = realmTimeZone
        self.orderBy = orderBy
        self._page = page
