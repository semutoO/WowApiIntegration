from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiAuctionRequests(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, connectedRealmId = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)        
        self.connectedRealmId = connectedRealmId
