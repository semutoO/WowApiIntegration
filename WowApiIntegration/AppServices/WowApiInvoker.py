import requests
from requests.auth import HTTPBasicAuth
from WowApiIntegration.Dto import AbstractWowApiRequest, AbstractWowApiResponse, WowApiAccessTokenModel, WowApiCredentialModel


class WowApiInvoker:
    def __init__(self,region="us", apiUrl="api.blizzard.com",creds=None):
        self.apiAccessToken:WowApiAccessTokenModel.WowApiAccessTokenModel = None
        self.region = region.lower()
        self.apiUrl = apiUrl
        self.apiCreds:WowApiCredentialModel.WowApiCredentialModel = creds

    def GetApiUrl(self):
        return "https://" + self.region + "." + self.apiUrl.lstrip(".")
    
    def DoWithInvoker(self, apiWork): 
        try:
            if(self.apiAccessToken is None or self.apiAccessToken.IsTokenExpired(self.apiAccessToken)):
                accToken = self.GetWowAccessToken()        
            else:
                accToken = self.apiAccessToken.accessToken
                    
            headers = { "Authorization" : "Bearer %s" % accToken }
            reqClient = requests.Session()
            reqClient.headers = headers
            return apiWork(reqClient)
        except Exception as ex:
            raise ex

    def DoWork(self, reqClient, endpoint, urlParams):
        response = reqClient.get(self.GetApiUrl() + endpoint, params=urlParams)        
        workResponse = AbstractWowApiResponse.AbstractWowApiResponse
        
        if(response.status_code != 200):
            workResponse.success = False
            workResponse.errorMessage = response
            return workResponse
        
        workResponse.response = response.json()
        return workResponse 
    
    def GetAbstractRequestParams(self, request:AbstractWowApiRequest.AbstractWowApiRequest):
        params = dict()
        params["region"] = request.region
        params["namespace"] = request.namespace
        params["locale"] = request.locale                
        return params

    def AddRequestParamsFromRequestObject(self, request):
        params = dict()

        for attr, val in vars(request).items():
            if(not attr.startswith("__")):
                params[attr] = val

        # for attr in dir(request):
        #     if(not attr.startswith("__")):
        #         val = getattr(request,attr)                
        #         params[attr] = val
        
        # Bug to work out going this route where looping the modules might set base values in first (profile set first, then dynamic)
        # requestProperties = {}
        # for base in request.__mro__:
        #     if(request.__module__ == base.__module__):
        #         requestProperties.update(vars(base))

        # for derivedAttr, derivedVal in vars(request).items():
        #     if(derivedAttr in requestProperties):
        #         requestProperties[derivedAttr] = derivedVal

        # #for attr, val in request.__dict__.items():
        # for attr, val in requestProperties.items():
        #     if(not attr.startswith("__")):
        #         if(val is not None and val):
        #             params[attr] = val
        return params
    
    def CallApi(self, request):
        params = self.AddRequestParamsFromRequestObject(request)
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))

    def GetWowAccessToken(self):
        url = "https://%s.battle.net/oauth/token" % self.region
        body = {"grant_type": 'client_credentials', "scope": "wow.profile" }
        auth = HTTPBasicAuth(self.apiCreds.clientId, self.apiCreds.clientSecret)
        response = requests.post(url, data=body, auth=auth)

        if(response.status_code != 200):            
            raise Exception("An error occurred retrieving the access token")            
        else:
            response = response.json()
            self.apiAccessToken = WowApiAccessTokenModel.WowApiAccessTokenModel(response["access_token"], response["expires_in"], response["sub"], response["token_type"])        
            return self.apiAccessToken.accessToken