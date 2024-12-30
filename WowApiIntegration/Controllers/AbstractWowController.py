from WowApiIntegration.AppServices import WowApiInvoker
from WowApiIntegration.Dto import AbstractWowApiResponse, WowApiCredentialModel

class AbstractWowController:
    creds = WowApiCredentialModel    

    def __init__(self, wowCreds: WowApiCredentialModel):
        self.creds = wowCreds
        
    def ApiInvoker(self, request, invokerEndpoint):
        try:
            wowApiInvoker = WowApiInvoker.WowApiInvoker(creds=self.creds)            
            invokerResponse:AbstractWowApiResponse.AbstractWowApiResponse = wowApiInvoker.CallApi(request)
            #invokerResponse:AbstractWowApiResponse.AbstractWowApiResponse = invokerEndpoint(wowApiInvoker, request)
            #invokerResponse:AbstractWowApiResponse.AbstractWowApiResponse = getattr(wowApiInvoker,invokerEndpoint)(request)
            return invokerResponse
        except Exception as ex:
            return "An error occurred calling %s." % invokerEndpoint