from WowApiIntegration.AppServices import WowApiInvoker
from WowApiIntegration.Controllers import AbstractWowController
from WowApiIntegration.Dto import AbstractWowApiRequest
from WowApiIntegration.Dto.GameDataDto import WowApiAchievementRequest, WowApiAuctionRequests, WowApiConnectedRealmRequest, WowApiCovenantRequest, WowApiCreatureRequest, WowApiGuildCrestRequest, WowApiItemAppearanceRequest, WowApiItemRequest, WowApiJournalRequest, WowApiModifiedCraftingRequest, WowApiMountRequest, WowApiMythicKeystoneAffixRequest, WowApiMythicKeystoneDungeonLeaderboardRequest, WowApiMythicKeystoneDungeonRequest, WowApiMythicRaidLeaderboardRequest, WowApiPetRequest, WowApiPlayableClassRequest, WowApiPlayableRaceRequest, WowApiPlayableSpecializationRequest, WowApiPowerTypeRequest

class WowGameDataController(AbstractWowController.AbstractWowController):        
    def SetEndpointIfNone(requestEndpoint, defaultEndpoint):
        requestEndpoint = defaultEndpoint if requestEndpoint is None else requestEndpoint
#region Achievements
    def GetAchievementIndex(self):
        request = WowApiAchievementRequest.WowApiAchievementRequest(endpoint="/data/wow/achievement/index")        
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementIndex)        
        return response
    
    def GetAchievement(self):
        request = WowApiAchievementRequest.WowApiAchievementRequest(endpoint = "/data/wow/achievement/%s" % request.achievementId)        
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievement)
        return response
    
    def GetAchievementMedia(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        request = WowApiAchievementRequest.WowApiAchievementRequest(endpoint = "/data/wow/media/achievement/%s" % request.achievementId)
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementMedia)
        return response
    
    def GetAchievementCategoryIndex(self, request:AbstractWowApiRequest.AbstractWowApiRequest):
        request = AbstractWowApiRequest.AbstractWowApiRequest(endpoint = "/data/wow/achievement-category/index")        
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Auction House
    def GetAuctions(self, request:WowApiAuctionRequests.WowApiAuctionRequests):        
        #request = AbstractWowApiRequest.AbstractWowApiRequest(endpoint = "/data/wow/connected-realm/%s/auctions" % request.connectedRealmId)
        request.endpoint = "/data/wow/connected-realm/%s/auctions" % request.connectedRealmId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCommodities(self, request:WowApiAuctionRequests.WowApiAuctionRequests):        
        #request = AbstractWowApiRequest.AbstractWowApiRequest(endpoint = "/data/wow/auctions/commodities")
        request.endpoint = "/data/wow/auctions/commodities" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Connected Realm 
    def GetConnectedRealmIndex(self, request:WowApiConnectedRealmRequest.WowApiConnectedRealmRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm/index")
        request.endpoint = "/data/wow/connected-realm/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetConnectedRealm(self, request:WowApiConnectedRealmRequest.WowApiConnectedRealmRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm/%s" % request.connectedRealmId)
        request.endpoint = "/data/wow/connected-realm/%s" % request.connectedRealmId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def ConnectedRealmSearch(self, request:WowApiConnectedRealmRequest.WowApiConnectedRealmRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/connected-realm" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Covenant
    def GetCovenantIndex(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/covenant/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCovenant(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/covenant/%s" % request.covenantId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCovenantMedia(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/covenant/%s" % request.covenantId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetSoulbindIndex(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/covenant/soulbind/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetSoulbind(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/covenant/soulbind/%s" % request.soulbindId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetConduitIndex(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/covenant/conduit/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetConduit(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/covenant/conduit/%s" % request.soulbindId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Creature
    def GetCreature(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/creature/%s" % request.creatureId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureSearch(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/search/creature" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureDisplayMedia(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/creature-display/%s" % request.creatureDisplayId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureFamilyIndex(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/creature-family/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureFamily(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/creature-family/%s" % request.creatureFamilyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureFamilyMedia(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/creature-family/%s" % request.creatureFamilyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureTypeIndex(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/creature-type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetCreatureType(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/creature-type/%s" % request.creatureFamilyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Guild Crest
    def GetGuildCrestComponentIndex(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/guild-crest/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetGuildCrestBorderMedia(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/guild-crest/border/%s" % request.borderId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetGuildCrestEmblemMedia(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/guild-crest/emblem/%s" % request.emblemId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Heirloom
    def GetHeirloomIndex(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/heirloom/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetHeirloom(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/heirloom/%s" % request.heirloomId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Item
    def GetItem(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item/%s" % request.itemId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemSearch(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/search/item" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemMedia(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/item/%s" % request.itemId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemClassesIndex(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-class/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemClass(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-class/%s" % request.itemClassId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemSetIndex(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-set/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemSet(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-set/%s" % request.itemSetId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemSubclass(self, request:WowApiItemRequest.WowApiItemRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = f"/data/wow/item-class/{request.itemClassId}/item-subclass/{request.itemSubclassId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Item Appearance
    def GetItemAppearance(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-appearance/%s" % request.appearanceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemAppearanceSearch(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/search/item-appearance" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemAppearanceSetsIndex(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-appearance/set/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemAppearanceSet(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-appearance/set/%s" % request.appearanceSetId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemAppearanceSlotIndex(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-appearance/slot/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetItemAppearanceSlot(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/item-appearance/slot/%s" % request.slotType if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response    
#endregion

#region Journal
    def GetJournalExpansionsIndex(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/journal-expansion/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalExpansion(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/journal-expansion/%s" % request.journalExpansionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalEncountersIndex(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/journal-encounter/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalEncounter(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/journal-encounter/%s" % request.journalEncounterId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalEncounterSearch(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/search/journal-encounter" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalInstancesIndex(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/journal-instance/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalInstance(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/journal-instance/%s" % request.journalInstanceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetJournalInstanceMedia(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/journal-instance/%s" % request.journalInstanceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Media Search
    def GetMediaSearch(self, request:AbstractWowApiRequest.AbstractWowApiRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/search/media" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Modified Crafting
    def GetModifiedCraftingIndex(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/modified-crafting/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetModifiedCraftingCategoryIndex(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/modified-crafting/category/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetModifiedCraftingCategory(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/modified-crafting/category/%s" % request.categoryId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetModifiedCraftingReagentSlotTypeIndex(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/modified-crafting/reagent-slot-type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetModifiedCraftingReagentSlotType(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/modified-crafting/reagent-slot-type/%s" % request.slotTypeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Mount
    def GetMountsIndex(self, request:WowApiMountRequest.WowApiMountRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mount/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMount(self, request:WowApiMountRequest.WowApiMountRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mount/%s" % request.mountId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMountSearch(self, request:WowApiMountRequest.WowApiMountRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/search/mount" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Mythic Keystone Affix
    def GetMythicKeystoneAffixesIndex(self, request:WowApiMythicKeystoneAffixRequest.WowApiMythicKeystoneAffixRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/keystone-affix/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneAffix(self, request:WowApiMythicKeystoneAffixRequest.WowApiMythicKeystoneAffixRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/keystone-affix/%s" % request.keystoneAffixId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneAffixMedia(self, request:WowApiMythicKeystoneAffixRequest.WowApiMythicKeystoneAffixRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/keystone-affix/%s" % request.keystoneAffixId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Mythic Keystone Dungeon
    def GetMythicKeystoneIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneDungeonsIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/dungeon/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneDungeon(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/dungeon/%s" % request.dungeonId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystonePeriodsIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/period/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystonePeriod(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/period/%s" % request.periodId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneSeasonsIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/season/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneSeason(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/mythic-keystone/season/%s" % request.seasonId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Mythic Keystone Leaderboard
    def GetMythicKeystoneLeaderboardsIndex(self, request:WowApiMythicKeystoneDungeonLeaderboardRequest.WowApiMythicKeystoneDungeonLeaderboardRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = f"/data/wow/connected-realm/{request.connectedRealmId}/mythic-leaderboard/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetMythicKeystoneLeaderboard(self, request:WowApiMythicKeystoneDungeonLeaderboardRequest.WowApiMythicKeystoneDungeonLeaderboardRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = f"/data/wow/connected-realm/{request.connectedRealmId}/mythic-leaderboard/{request.dungeonId}/period/{request.periodId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Mythic Raid Leaderboard
    def GetMythicRaidLeaderboard(self, request:WowApiMythicRaidLeaderboardRequest.WowApiMythicRaidLeaderboardRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = f"/data/wow/leaderboard/hall-of-fame/{request.raid}/{request.faction}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Pet
    def GetPetsIndex(self, request:WowApiPetRequest.WowApiPetRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/pet/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetPet(self, request:WowApiPetRequest.WowApiPetRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/pet/%s" % request.petId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetPetMedia(self, request:WowApiPetRequest.WowApiPetRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/pet/%s" % request.petId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetPetAbilitiesIndex(self, request:WowApiPetRequest.WowApiPetRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/pet-ability/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetPetAbility(self, request:WowApiPetRequest.WowApiPetRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/pet-ability/%s" % request.petAbilityId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetPetAbilityMedia(self, request:WowApiPetRequest.WowApiPetRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/pet-ability/%s" % request.petAbilityId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Playable Class
    def GetPlayableClassIndex(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-class/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response

    def GetPlayableClass(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-class/%s" % request.classId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response

    def GetPlayableClassMedia(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/playable-class/%s" % request.playableClassId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response        
    
    def GetPvpTalentSlots(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-class/%s/pvp-talent-slots" % request.classId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Playable Race
    def GetPlayableRacesIndex(self, request:WowApiPlayableRaceRequest.WowApiPlayableRaceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-race/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
    
    def GetPlayableRaces(self, request:WowApiPlayableRaceRequest.WowApiPlayableRaceRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-race/%s" % request.playableRaceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Playable Specialization
    def GetPlayableSpecializatonsIndex(self, request:WowApiPlayableSpecializationRequest.WowApiPlayableSpecializationRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-specializations/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response

    def GetPlayableSpecialization(self, request:WowApiPlayableSpecializationRequest.WowApiPlayableSpecializationRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/playable-specializations/%s" % request.specId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response

    def GetPlayableSpecializationMedia(self, request:WowApiPlayableSpecializationRequest.WowApiPlayableSpecializationRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/media/playable-specializations/%s" % request.specId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response        
#endregion

#region Power Type
    def GetPowerTypesIndex(self, request:WowApiPowerTypeRequest.WowApiPowerTypeRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/power-type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response

    def GetPowerType(self, request:WowApiPowerTypeRequest.WowApiPowerTypeRequest):        
        #request = WowApiConnectedRealmRequests.WowApiConnectedRealmRequests(endpoint = "/data/wow/connected-realm")
        request.endpoint = "/data/wow/power-type/%s" % request.powerTypeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request, WowApiInvoker.WowApiInvoker.GetAchievementCategoryIndex)
        return response
#endregion

#region Profession

#endregion
    def WowTokenTest(self):
        tokenRequest = WowApiPowerTypeRequest.WowApiPowerTypeRequest
        tokenRequest.endpoint = "/data/wow/token/index"
        tokenPriceResponse = self.ApiInvoker(tokenRequest, None)        
        return tokenPriceResponse.response["price"] / 10000 if tokenPriceResponse.success else tokenPriceResponse.errorMessage

    def GetWowTokenIndex(self):
        tokenRequest = AbstractWowApiRequest.AbstractWowApiRequest
        tokenPriceResponse = self.ApiInvoker(tokenRequest, "GetWowTokenPrice")        
        return tokenPriceResponse.response / 10000 if tokenPriceResponse.success else tokenPriceResponse.errorMessage