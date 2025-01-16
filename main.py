import json
from WowApiIntegration.Controllers import WowCharacterProfileController, WowGameDataController
from WowApiIntegration.Dto import WowApiCredentialModel
from WowApiIntegration.Dto.GameDataDto import WowApiAuctionRequests, WowApiConnectedRealmRequest, WowApiItemRequest, WowApiPlayableClassRequest, WowApiPlayableRaceRequest, WowApiWowTokenRequest
from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest, WowApiCharEquipSumRequest, WowApiCharacterProfileRequest

with open("wowApiConfig.json") as f:
    configSettings = json.load(f)    
wowCreds = WowApiCredentialModel.WowApiCredentialModel(configSettings["clientId"],configSettings["clientSecret"])

#region GameData test calls
#controller = WowGameDataController.WowGameDataController(wowCreds)
#getThunderfury = controller.GetItem(WowApiItemRequest.WowApiItemRequest(itemId = 19019))
#print(getThunderfury)
#searchItemResponse = controller.GetItemSearch(WowApiItemRequest.WowApiItemSearchRequest(locale="en_US", searchDict = {"id":"[1,1000]"}))
#print(searchItemResponse)
#getConnRealmInd = controller.GetConnectedRealmIndex(WowApiConnectedRealmRequest.WowApiConnectedRealmRequest(connectedRealmId=1000))
#print(getConnRealmId)
#getConnRealm = controller.GetConnectedRealm(WowApiConnectedRealmRequest.WowApiConnectedRealmRequest(connectedRealmId=106))
#print(getConnRealm)
#connRealmSearchByTz = controller.ConnectedRealmSearch(WowApiConnectedRealmRequest.WowApiConnectedRealmSearchRequest(searchDict={"realms.timezone" : "America/New_York"}))
#print(connRealmSearchByTz)
#connRealmSearchBySlug = controller.ConnectedRealmSearch(WowApiConnectedRealmRequest.WowApiConnectedRealmSearchRequest(searchDict={"realms.slug" : "realmSlug"}))
#print(connRealmSearchBySlug)
# tokenReq = WowApiWowTokenRequest.WowApiWowTokenRequest()
# tokenPrice = controller.GetWowTokenIndex(tokenReq)
# print(tokenPrice)
#endregion

#region Character Profile test calls
# charProfController = WowCharacterProfileController.WowCharacterProfileController(wowCreds)
# charEqReq = WowApiCharEquipSumRequest.WowApiCharEquipSumRequest(charName="charName", realmSlug="realmSlug")
# charEq = charProfController.GetCharacterEquipmentSummary(charEqReq)
# print(charEq)
# charMediaRequest = WowApiCharacterProfileRequest.WowApiCharacterProfileRequest(charName="charName", realmSlug="realmSlug")
# charMed = charProfController.GetCharacterProfileStatus(charMediaRequest)
# print(charMed)
#endregion