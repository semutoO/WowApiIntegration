from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiAuctionRequests(AbstractWowApiRequest.AbstractWowApiRequest):
    connectedRealmId = None

    def __init__(self, endpoint, connectedRealmId = None, region="us", namespace="dynamic-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.connectedRealmId = connectedRealmId
