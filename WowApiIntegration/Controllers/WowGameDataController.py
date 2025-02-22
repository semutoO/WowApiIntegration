from WowApiIntegration.Dto import WowApiCredentialModel, WowApiInvoker, WowApiTokenRequest

class WowGameDataController:
    creds = WowApiCredentialModel    

    def __init__(self, wowCreds: WowApiCredentialModel):
        self.creds = wowCreds

    def FetchTokenPrice(self):
        try:
            tokenRequest = WowApiTokenRequest.WowApiTokenRequest
            wowApiConfig = WowApiInvoker.WowApiInvoker(creds=self.creds)        
            tokenPrice = wowApiConfig.GetWowTokenPrice(tokenRequest)        
            return tokenPrice / 10000
        except Exception as ex:
            return "An error occurred fetching token prices. %s" % str(ex)