from WowApiIntegration.Dto import WowApiCharacterProfileRequest, WowApiCredentialModel, WowApiInvoker, WowApiTokenRequest

class WowCharacterProfileController:
    creds = WowApiCredentialModel    

    def __init__(self, wowCreds: WowApiCredentialModel):
        self.creds = wowCreds

    def FetchCharacterRender(self):
        try:
            charRequest = WowApiCharacterProfileRequest.WowApiCharacterProfileRequest("us","moonrunner","kagurå","profile-us","en_US","status")            
            wowApiConfig = WowApiInvoker.WowApiInvoker(creds=self.creds)
            charMediaResponse = wowApiConfig.GetCharacterMediaSummary(charRequest)
            return charMediaResponse
        except Exception as ex:
            return "An error occurred fetching token prices. %s" % str(ex)