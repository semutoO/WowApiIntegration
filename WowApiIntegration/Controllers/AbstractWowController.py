from WowApiIntegration.AppServices import WowApiInvoker
from WowApiIntegration.Dto import AbstractWowApiResponse, WowApiCredentialModel

class AbstractWowController:
    creds = WowApiCredentialModel    

    def __init__(self, wowCreds: WowApiCredentialModel):
        self.creds = wowCreds

    def ApiInvoker(self, request):
        try:
            wowApiInvoker = WowApiInvoker.WowApiInvoker(creds=self.creds)            
            invokerResponse:AbstractWowApiResponse.AbstractWowApiResponse = wowApiInvoker.CallApi(request)            
            return invokerResponse
        except Exception as ex:
            return "An error occurred calling %s." % request.endpoint    