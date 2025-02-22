import json
from WowApiIntegration.Controllers import WowCharacterProfileController, WowGameDataController
from WowApiIntegration.Dto import WowApiCredentialModel

with open("wowApiConfig.json") as f:
    configSettings = json.load(f)    
wowCreds = WowApiCredentialModel.WowApiCredentialModel(configSettings["clientId"],configSettings["clientSecret"])

controller = WowGameDataController.WowGameDataController(wowCreds)
tokenPrice = controller.FetchTokenPrice()
charProfController = WowCharacterProfileController.WowCharacterProfileController(wowCreds)
chPro = charProfController.FetchCharacterRender()