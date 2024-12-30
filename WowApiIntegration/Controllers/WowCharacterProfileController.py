from WowApiIntegration.Controllers import AbstractWowController
from WowApiIntegration.Dto.ProfileDto import WowApiCharacterProfileRequest

class WowCharacterProfileController(AbstractWowController.AbstractWowController):
    def GetCharacterRender(self):
        try:
            charRequest = WowApiCharacterProfileRequest.WowApiCharacterProfileRequest("us","moonrunner","kagurå","profile-us","en_US","status")                        
            charMediaResponse = self.ApiInvoker(charRequest, "GetCharacterMediaSummary")
            return charMediaResponse
        except Exception as ex:
            return "An error occurred fetching token prices. %s" % str(ex)