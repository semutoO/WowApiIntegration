from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiConnectedRealmRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    connectedRealmId = None
    status = None
    realmTimeZone = "America/New_York"
    orderBy = "id"
    _page = 1

    def __init__(self, endpoint, status = None, realmTimeZone = "America/New_York", orderBy = "id", page = 1, connectedRealmId = None, region="us", namespace="dynamic-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.connectedRealmId = connectedRealmId
        self.status = status
        self.realmTimeZone = realmTimeZone
        self.orderBy = orderBy
        self._page = page
