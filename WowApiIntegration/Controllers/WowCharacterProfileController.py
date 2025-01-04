from WowApiIntegration.Controllers import AbstractWowController
from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest, WowApiCharEquipSumRequest, WowApiCharacterProfileRequest

class WowCharacterProfileController(AbstractWowController.AbstractWowController):
    #Missing something for authentication around wow.profile scope probably
    def GetAccountToysCollectionSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        try:
            request.endpoint = "/profile/user/wow/collections/toys"
            response = self.ApiInvoker(request)
            return response
        except Exception as ex:
            return "Nope"

    def GetCharacterMediaSummary(self, request:WowApiCharacterProfileRequest.WowApiCharacterProfileRequest):
        try:
            request.endpoint = f"/profile/wow/character/{request.realmSlug}/{request.characterName}/character-media"            
            charMediaResponse = self.ApiInvoker(request)
            return charMediaResponse
        except Exception as ex:
            return "An error occurred fetching token prices. %s" % str(ex)
        
    def GetCharacterProfileStatus(self, request:WowApiCharacterProfileRequest.WowApiCharacterProfileRequest):
        try:
            request.endpoint = f"/profile/wow/character/{request.realmSlug}/{request.characterName}/status"            
            charMediaResponse = self.ApiInvoker(request)
            return charMediaResponse
        except Exception as ex:
            return "An error occurred fetching token prices. %s" % str(ex)
        
    def GetCharacterEquipmentSummary(self, request:WowApiCharEquipSumRequest.WowApiCharEquipSumRequest):
        request.endpoint = f"/profile/wow/character/{request.realmSlug}/{request.characterName}/equipment" 
        response = self.ApiInvoker(request)        
        return response.response if response.success else response.errorMessage