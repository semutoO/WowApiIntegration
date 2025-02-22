from WowApiIntegration.Controllers import AbstractWowController
from WowApiIntegration.Dto.ProfileDto import AbstractWowApiProfileRequest, WowApiAccountProfileRequest, WowApiCharacterAchievementRequest, WowApiCharacterAppearanceRequest, WowApiCharacterCollectionRequest, WowApiCharacterProfileRequest, WowApiCharacterPvpRequest, WowApiGuildRequest

class WowCharacterProfileController(AbstractWowController.AbstractWowController):
#region Account Profile
    def GetAccountProfileSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint="/profile/user/wow" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetProtectedCharacterProfileSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/protected-character/{request.realmId}-{request.characterId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetAccountCollectionsIndex(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/collections" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetAccountHeirloomsCollectionSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/collections/heirlooms" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetAccountMountsCollectionSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/collections/mounts" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetAccountPetsCollectionSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/collections/pets" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetAccountToysCollectionSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/collections/toys" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetAccounTransmogCollectionSummary(self, request:WowApiAccountProfileRequest.WowApiAccountProfileRequest):
        request.endpoint=f"/profile/user/wow/collections/transmogs" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Character Achievements
    def GetCharacterAchievementsSummary(self, request:WowApiCharacterAchievementRequest.WowApiCharacterAchievementRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/achievements" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetCharacterAchievementsStatistics(self, request:WowApiCharacterAchievementRequest.WowApiCharacterAchievementRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/achievements/statistics" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response            
#endregion

#region Character Appearance
    def GetCharacterAppearanceSummary(self, request:WowApiCharacterAppearanceRequest.WowApiCharacterAppearanceRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/achievements" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Character Collections
    def GetCharacterCollectionsIndex(self, request:WowApiCharacterCollectionRequest.WowApiCharacterCollectionRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/collections" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetCharacterHeirloomsCollectionSummary(self, request:WowApiCharacterCollectionRequest.WowApiCharacterCollectionRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/collections/heirlooms" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetCharacterMountsCollectionSummary(self, request:WowApiCharacterCollectionRequest.WowApiCharacterCollectionRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/collections/mounts" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetCharacterPetsCollectionSummary(self, request:WowApiCharacterCollectionRequest.WowApiCharacterCollectionRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/collections/pets" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetCharacterToysCollectionSummary(self, request:WowApiCharacterCollectionRequest.WowApiCharacterCollectionRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/collections/toys" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetCharacterTransmogCollectionSummary(self, request:WowApiCharacterCollectionRequest.WowApiCharacterCollectionRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/collections/transmogs" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                
#endregion

#region Character Encounters
    def GetCharacterEncountersSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/encounters" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                
    
    def GetCharacterDungeons(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/encounters/dungeons" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
    
    def GetCharacterRaids(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/encounters/raids" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                        
#endregion

#region Character Equipment
    def GetCharacterEquipmentSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/equipment" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
#endregion

#region Character Hunter Pets
    def GetCharacterHunterPetsSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/hunter-pets" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
#endregion

#region Character Media
    def GetCharacterMediaSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/character-media" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
#endregion

#region Character Mythic Keystone Profile
    def GetCharacterMythicKeystoneProfileIndex(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/mythic-keystone-profile" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    

    def GetCharacterMythicKeystoneSeasonDetails(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/mythic-keystone-profile/season/{request.seasonId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
#endregion

#region Character Professions
    def GetCharacterProfessionsSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/professions" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
#endregion

#region Character Profile
    def GetCharacterProfileSummary(self, request:WowApiCharacterProfileRequest.WowApiCharacterProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                    
    
    def GetCharacterProfileStatus(self, request:WowApiCharacterProfileRequest.WowApiCharacterProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/status" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                        
#endregion

#region Character PVP
    def GetCharacterPvpBracketStatistics(self, request:WowApiCharacterPvpRequest.WowApiCharacterPvpRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/pvp-bracket/{request.pvpBracket}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                 

    def GetCharacterPvpSummary(self, request:WowApiCharacterPvpRequest.WowApiCharacterPvpRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/pvp-summary" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
#endregion

#region Character Quests
    def GetCharacterQuests(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/quests" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
    
    def GetCharacterCompletedQuests(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/quests/completed" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                       
#endregion

#region Character Reputation
    def GetCharacterReputationSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/reputations" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
#endregion

#region Character Soulbinds
    def GetCharacterSoulbinds(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/soulbinds" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
#endregion

#region Character Specializations
    def GetCharacterSpecializationsSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/specializations" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
#endregion

#region Character Statistics
    def GetCharacterStatisticsSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/statistics" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
#endregion

#region Character Titles
    def GetCharacterTitlesSummary(self, request:AbstractWowApiProfileRequest.AbstractWowApiProfileRequest):
        request.endpoint=f"/profile/wow/character/{request.realmSlug}/{request.characterName}/titles" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                   
#endregion

#region Guild
    def GetGuild(self, request:WowApiGuildRequest.WowApiGuildRequest):
        request.endpoint=f"/data/wow/guild/{request.realmSlug}/{request.nameSlug}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response      

    def GetGuildActivity(self, request:WowApiGuildRequest.WowApiGuildRequest):
        request.endpoint=f"/data/wow/guild/{request.realmSlug}/{request.nameSlug}/activity" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                                       
    
    def GetGuildAchievements(self, request:WowApiGuildRequest.WowApiGuildRequest):
        request.endpoint=f"/data/wow/guild/{request.realmSlug}/{request.nameSlug}/achievements" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response          
    
    def GetGuildRoster(self, request:WowApiGuildRequest.WowApiGuildRequest):
        request.endpoint=f"/data/wow/guild/{request.realmSlug}/{request.nameSlug}/roster" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response          
#endregion