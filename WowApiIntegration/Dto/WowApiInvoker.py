import requests
from requests.auth import HTTPBasicAuth
from WowApiIntegration.Dto import WowApiAccessTokenModel, WowApiCharacterProfileRequest, WowApiCredentialModel, WowApiTokenRequest


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
            return apiWork(reqClient, self.GetApiUrl())
        except Exception as ex:
            raise ex

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

    def GetWowTokenPrice(self, tokenRequest:WowApiTokenRequest.WowApiTokenRequest):
        return self.DoWithInvoker(lambda client, apiUrl : (self.TokenWork(client, apiUrl, tokenRequest)))                                
                           
    def TokenWork(self, reqClient, apiUrl, tokenRequest:WowApiTokenRequest.WowApiTokenRequest):            
        params = dict()
        params["region"] = tokenRequest.region
        params["namespace"] = tokenRequest.namespace
        params["locale"] = tokenRequest.locale        
        tokenResponse = reqClient.get(apiUrl + "/data/wow/token/index", params=params)                
        
        if(tokenResponse.status_code != 200):
            return 0
        
        return tokenResponse.json()["price"]

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