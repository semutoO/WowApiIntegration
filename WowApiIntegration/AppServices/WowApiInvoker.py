import requests
from requests.auth import HTTPBasicAuth
from WowApiIntegration.Dto import AbstractWowApiRequest, AbstractWowApiResponse, WowApiAccessTokenModel, WowApiAchievementRequest, WowApiCredentialModel
from WowApiIntegration.Dto.ProfileDto import WowApiCharacterProfileRequest


class WowApiInvoker:
    apiUrl = "api.blizzard.com"
    region = "us"
    apiCreds = WowApiCredentialModel.WowApiCredentialModel
    apiAccessToken = WowApiAccessTokenModel.WowApiAccessTokenModel

    def __init__(self,region="us", apiUrl="api.blizzard.com",creds=None):
        self.region = region.lower()
        self.apiUrl = apiUrl
        self.apiCreds = creds

    def GetApiUrl(self):
        return "https://" + self.region + "." + self.apiUrl.lstrip(".")
    
    def DoWithInvoker(self, apiWork): 
        try:
            if(self.apiAccessToken.IsTokenExpired(self.apiAccessToken)):
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
        requestProperties = {}
        for base in request.__mro__:
            requestProperties.update(vars(base))

        for derivedAttr, derivedVal in vars(request).items():
            if(derivedAttr in requestProperties):
                requestProperties[derivedAttr] = derivedVal

        #for attr, val in request.__dict__.items():
        for attr, val in requestProperties.items():
            if(not attr.startswith("__")):
                if(val is not None and val):
                    params[attr] = val
        return params
    
    def CallApi(self, request):
        params = self.AddRequestParamsFromRequestObject(request)
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))

#region Achievement Endpoints  
    def GetAchievementIndex(self, request:AbstractWowApiRequest.AbstractWowApiRequest):
        params = self.GetAbstractRequestParams(request)        
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))

    def GetAchievement(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        params = self.GetAbstractRequestParams(request)
        #params["achievementId"] = request.achievementId
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))

    def GetAchievementMedia(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        params = self.GetAbstractRequestParams(request)
        params["achivementId"] = request.achievementId
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))
    
    def GetAchievementCategoryIndex(self, request:AbstractWowApiRequest.AbstractWowApiRequest):
        params = self.GetAbstractRequestParams(request)
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))
    
    def GetAchievementCategory(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        params = self.GetAbstractRequestParams(request)
        params["achivementCategoryId"] = request.achievementCategoryId
        return self.DoWithInvoker(lambda client : (self.DoWork(client, request.endpoint, params)))
#endregion

    def GetWowAccessToken(self):
        url = "https://%s.battle.net/oauth/token" % self.region
        body = {"grant_type": 'client_credentials'}
        auth = HTTPBasicAuth(self.apiCreds.clientId, self.apiCreds.clientSecret)
        response = requests.post(url, data=body, auth=auth)

        if(response.status_code != 200):            
            raise Exception("An error occurred retrieving the access token")            
        else:
            response = response.json()
            self.apiAccessToken = WowApiAccessTokenModel.WowApiAccessTokenModel(response["access_token"], response["token_type"], response["expires_in"], response["sub"])        
            return self.apiAccessToken.accessToken

    def GetWowTokenPrice(self, tokenRequest:AbstractWowApiRequest.AbstractWowApiRequest):
        return self.DoWithInvoker(lambda client, apiUrl : (self.TokenWork(client, apiUrl, tokenRequest)))                                
                           
    def TokenWork(self, reqClient, apiUrl, tokenRequest:AbstractWowApiRequest.AbstractWowApiRequest):            
        params = dict()
        params["region"] = tokenRequest.region
        params["namespace"] = tokenRequest.namespace
        params["locale"] = tokenRequest.locale        
        tokenResponse = reqClient.get(apiUrl + "/data/wow/token/index", params=params)        
        workResponse = AbstractWowApiResponse.AbstractWowApiResponse
        
        if(tokenResponse.status_code != 200):
            workResponse.success = False
            workResponse.errorMessage = tokenResponse
            return workResponse
        
        workResponse.response = tokenResponse.json()["price"]
        return workResponse

    def GetCharacterMediaSummary(self, charMediaRequest:WowApiCharacterProfileRequest.WowApiCharacterProfileRequest):
        return self.DoWithInvoker(lambda client, apiUrl : (self.CharacterProfileWork(client, apiUrl, charMediaRequest)))
    
    def CharacterProfileWork(self, reqClient, apiUrl, charProfileRequest:WowApiCharacterProfileRequest.WowApiCharacterProfileRequest):    
        params = dict()
        params["region"] = charProfileRequest.region
        params["namespace"] = charProfileRequest.namespace
        params["locale"] = charProfileRequest.locale        
        
        charMediaResponse = reqClient.get(apiUrl + f"/profile/wow/character/{charProfileRequest.realmSlug}/{charProfileRequest.characterName}/{charProfileRequest.endpoint}", params=params)        

        if(charMediaResponse.status_code != 200):
            return None
        
        return charMediaResponse.json()