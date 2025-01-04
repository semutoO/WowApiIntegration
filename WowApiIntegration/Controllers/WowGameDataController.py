from WowApiIntegration.Controllers import AbstractWowController
from WowApiIntegration.Dto import AbstractWowApiRequest
from WowApiIntegration.Dto.GameDataDto import WowApiAchievementRequest, WowApiAuctionRequests, WowApiConnectedRealmRequest, WowApiCovenantRequest, WowApiCreatureRequest, WowApiGuildCrestRequest, WowApiItemAppearanceRequest, WowApiItemRequest, WowApiJournalRequest, WowApiModifiedCraftingRequest, WowApiMountRequest, WowApiMythicKeystoneAffixRequest, WowApiMythicKeystoneDungeonLeaderboardRequest, WowApiMythicKeystoneDungeonRequest, WowApiMythicRaidLeaderboardRequest, WowApiPetRequest, WowApiPlayableClassRequest, WowApiPlayableRaceRequest, WowApiPlayableSpecializationRequest, WowApiPowerTypeRequest, WowApiProfessionRequest, WowApiPvpSeasonRequest, WowApiPvpTierRequest, WowApiQuestRequest, WowApiRealmRequest, WowApiRegionRequest, WowApiReputationRequest, WowApiSpellRequest, WowApiTalentRequest, WowApiTechTalentRequest, WowApiTitleRequest, WowApiToyRequest, WowApiWowTokenRequest

class WowGameDataController(AbstractWowController.AbstractWowController):        
    def SetEndpointIfNone(requestEndpoint, defaultEndpoint):
        requestEndpoint = defaultEndpoint if requestEndpoint is None else requestEndpoint

#region Achievements
    def GetAchievementIndex(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        request.endpoint="/data/wow/achievement/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetAchievement(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        request.endpoint = "/data/wow/achievement/%s" % request.achievementId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetAchievementMedia(self, request:WowApiAchievementRequest.WowApiAchievementRequest):
        request.endpoint = "/data/wow/media/achievement/%s" % request.achievementId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetAchievementCategoryIndex(self, request:AbstractWowApiRequest.AbstractWowApiRequest):
        request.endpoint = "/data/wow/achievement-category/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Auction House
    def GetAuctions(self, request:WowApiAuctionRequests.WowApiAuctionRequests):        
        request.endpoint = "/data/wow/connected-realm/%s/auctions" % request.connectedRealmId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCommodities(self, request:WowApiAuctionRequests.WowApiAuctionRequests):        
        request.endpoint = "/data/wow/auctions/commodities" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Connected Realm 
    def GetConnectedRealmIndex(self, request:WowApiConnectedRealmRequest.WowApiConnectedRealmRequest):        
        request.endpoint = "/data/wow/connected-realm/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetConnectedRealm(self, request:WowApiConnectedRealmRequest.WowApiConnectedRealmRequest):        
        request.endpoint = "/data/wow/connected-realm/%s" % request.connectedRealmId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def ConnectedRealmSearch(self, request:WowApiConnectedRealmRequest.WowApiConnectedRealmRequest):        
        request.endpoint = "/data/wow/connected-realm" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Covenant
    def GetCovenantIndex(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/covenant/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCovenant(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/covenant/%s" % request.covenantId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCovenantMedia(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/media/covenant/%s" % request.covenantId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetSoulbindIndex(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/covenant/soulbind/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetSoulbind(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/covenant/soulbind/%s" % request.soulbindId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetConduitIndex(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/covenant/conduit/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetConduit(self, request:WowApiCovenantRequest.WowApiCovenantRequest):        
        request.endpoint = "/data/wow/covenant/conduit/%s" % request.soulbindId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Creature
    def GetCreature(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/creature/%s" % request.creatureId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureSearch(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/search/creature" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureDisplayMedia(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/media/creature-display/%s" % request.creatureDisplayId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureFamilyIndex(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/creature-family/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureFamily(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/creature-family/%s" % request.creatureFamilyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureFamilyMedia(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/media/creature-family/%s" % request.creatureFamilyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureTypeIndex(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/creature-type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetCreatureType(self, request:WowApiCreatureRequest.WowApiCreatureRequest):        
        request.endpoint = "/data/wow/creature-type/%s" % request.creatureFamilyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Guild Crest
    def GetGuildCrestComponentIndex(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        request.endpoint = "/data/wow/guild-crest/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetGuildCrestBorderMedia(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        request.endpoint = "/data/wow/media/guild-crest/border/%s" % request.borderId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetGuildCrestEmblemMedia(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        request.endpoint = "/data/wow/media/guild-crest/emblem/%s" % request.emblemId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Heirloom
    def GetHeirloomIndex(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        request.endpoint = "/data/wow/heirloom/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetHeirloom(self, request:WowApiGuildCrestRequest.WowApiGuildCrestRequest):        
        request.endpoint = "/data/wow/heirloom/%s" % request.heirloomId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Item
    def GetItem(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/item/%s" % request.itemId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemSearch(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/search/item" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemMedia(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/media/item/%s" % request.itemId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemClassesIndex(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/item-class/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemClass(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/item-class/%s" % request.itemClassId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemSetIndex(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/item-set/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemSet(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = "/data/wow/item-set/%s" % request.itemSetId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemSubclass(self, request:WowApiItemRequest.WowApiItemRequest):        
        request.endpoint = f"/data/wow/item-class/{request.itemClassId}/item-subclass/{request.itemSubclassId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Item Appearance
    def GetItemAppearance(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        request.endpoint = "/data/wow/item-appearance/%s" % request.appearanceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemAppearanceSearch(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        request.endpoint = "/data/wow/search/item-appearance" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemAppearanceSetsIndex(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        request.endpoint = "/data/wow/item-appearance/set/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemAppearanceSet(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        request.endpoint = "/data/wow/item-appearance/set/%s" % request.appearanceSetId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemAppearanceSlotIndex(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        request.endpoint = "/data/wow/item-appearance/slot/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetItemAppearanceSlot(self, request:WowApiItemAppearanceRequest.WowApiItemAppearanceRequest):        
        request.endpoint = "/data/wow/item-appearance/slot/%s" % request.slotType if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
#endregion

#region Journal
    def GetJournalExpansionsIndex(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/journal-expansion/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalExpansion(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/journal-expansion/%s" % request.journalExpansionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalEncountersIndex(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/journal-encounter/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalEncounter(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/journal-encounter/%s" % request.journalEncounterId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalEncounterSearch(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/search/journal-encounter" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalInstancesIndex(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/journal-instance/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalInstance(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/journal-instance/%s" % request.journalInstanceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetJournalInstanceMedia(self, request:WowApiJournalRequest.WowApiJournalRequest):        
        request.endpoint = "/data/wow/media/journal-instance/%s" % request.journalInstanceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Media Search
    def GetMediaSearch(self, request:AbstractWowApiRequest.AbstractWowApiRequest):        
        request.endpoint = "/data/wow/search/media" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Modified Crafting
    def GetModifiedCraftingIndex(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        request.endpoint = "/data/wow/modified-crafting/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetModifiedCraftingCategoryIndex(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        request.endpoint = "/data/wow/modified-crafting/category/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetModifiedCraftingCategory(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        request.endpoint = "/data/wow/modified-crafting/category/%s" % request.categoryId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetModifiedCraftingReagentSlotTypeIndex(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        request.endpoint = "/data/wow/modified-crafting/reagent-slot-type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetModifiedCraftingReagentSlotType(self, request:WowApiModifiedCraftingRequest.WowApiModifiedCraftingRequest):        
        request.endpoint = "/data/wow/modified-crafting/reagent-slot-type/%s" % request.slotTypeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Mount
    def GetMountsIndex(self, request:WowApiMountRequest.WowApiMountRequest):        
        request.endpoint = "/data/wow/mount/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMount(self, request:WowApiMountRequest.WowApiMountRequest):        
        request.endpoint = "/data/wow/mount/%s" % request.mountId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMountSearch(self, request:WowApiMountRequest.WowApiMountRequest):        
        request.endpoint = "/data/wow/search/mount" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Mythic Keystone Affix
    def GetMythicKeystoneAffixesIndex(self, request:WowApiMythicKeystoneAffixRequest.WowApiMythicKeystoneAffixRequest):        
        request.endpoint = "/data/wow/keystone-affix/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneAffix(self, request:WowApiMythicKeystoneAffixRequest.WowApiMythicKeystoneAffixRequest):        
        request.endpoint = "/data/wow/keystone-affix/%s" % request.keystoneAffixId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneAffixMedia(self, request:WowApiMythicKeystoneAffixRequest.WowApiMythicKeystoneAffixRequest):        
        request.endpoint = "/data/wow/media/keystone-affix/%s" % request.keystoneAffixId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Mythic Keystone Dungeon
    def GetMythicKeystoneIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneDungeonsIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/dungeon/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneDungeon(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/dungeon/%s" % request.dungeonId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystonePeriodsIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/period/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystonePeriod(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/period/%s" % request.periodId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneSeasonsIndex(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/season/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneSeason(self, request:WowApiMythicKeystoneDungeonRequest.WowApiMythicKeystoneDungeonRequest):        
        request.endpoint = "/data/wow/mythic-keystone/season/%s" % request.seasonId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Mythic Keystone Leaderboard
    def GetMythicKeystoneLeaderboardsIndex(self, request:WowApiMythicKeystoneDungeonLeaderboardRequest.WowApiMythicKeystoneDungeonLeaderboardRequest):        
        request.endpoint = f"/data/wow/connected-realm/{request.connectedRealmId}/mythic-leaderboard/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetMythicKeystoneLeaderboard(self, request:WowApiMythicKeystoneDungeonLeaderboardRequest.WowApiMythicKeystoneDungeonLeaderboardRequest):        
        request.endpoint = f"/data/wow/connected-realm/{request.connectedRealmId}/mythic-leaderboard/{request.dungeonId}/period/{request.periodId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Mythic Raid Leaderboard
    def GetMythicRaidLeaderboard(self, request:WowApiMythicRaidLeaderboardRequest.WowApiMythicRaidLeaderboardRequest):        
        request.endpoint = f"/data/wow/leaderboard/hall-of-fame/{request.raid}/{request.faction}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Pet
    def GetPetsIndex(self, request:WowApiPetRequest.WowApiPetRequest):        
        request.endpoint = "/data/wow/pet/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPet(self, request:WowApiPetRequest.WowApiPetRequest):        
        request.endpoint = "/data/wow/pet/%s" % request.petId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPetMedia(self, request:WowApiPetRequest.WowApiPetRequest):        
        request.endpoint = "/data/wow/media/pet/%s" % request.petId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPetAbilitiesIndex(self, request:WowApiPetRequest.WowApiPetRequest):        
        request.endpoint = "/data/wow/pet-ability/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPetAbility(self, request:WowApiPetRequest.WowApiPetRequest):        
        request.endpoint = "/data/wow/pet-ability/%s" % request.petAbilityId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPetAbilityMedia(self, request:WowApiPetRequest.WowApiPetRequest):        
        request.endpoint = "/data/wow/media/pet-ability/%s" % request.petAbilityId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Playable Class
    def GetPlayableClassIndex(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        request.endpoint = "/data/wow/playable-class/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetPlayableClass(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        request.endpoint = "/data/wow/playable-class/%s" % request.classId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetPlayableClassMedia(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        request.endpoint = "/data/wow/media/playable-class/%s" % request.playableClassId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetPvpTalentSlots(self, request:WowApiPlayableClassRequest.WowApiPlayableClassRequest):        
        request.endpoint = "/data/wow/playable-class/%s/pvp-talent-slots" % request.classId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Playable Race
    def GetPlayableRacesIndex(self, request:WowApiPlayableRaceRequest.WowApiPlayableRaceRequest):        
        request.endpoint = "/data/wow/playable-race/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPlayableRaces(self, request:WowApiPlayableRaceRequest.WowApiPlayableRaceRequest):        
        request.endpoint = "/data/wow/playable-race/%s" % request.playableRaceId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Playable Specialization
    def GetPlayableSpecializatonsIndex(self, request:WowApiPlayableSpecializationRequest.WowApiPlayableSpecializationRequest):        
        request.endpoint = "/data/wow/playable-specializations/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetPlayableSpecialization(self, request:WowApiPlayableSpecializationRequest.WowApiPlayableSpecializationRequest):        
        request.endpoint = "/data/wow/playable-specializations/%s" % request.specId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetPlayableSpecializationMedia(self, request:WowApiPlayableSpecializationRequest.WowApiPlayableSpecializationRequest):        
        request.endpoint = "/data/wow/media/playable-specializations/%s" % request.specId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Power Type
    def GetPowerTypesIndex(self, request:WowApiPowerTypeRequest.WowApiPowerTypeRequest):        
        request.endpoint = "/data/wow/power-type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetPowerType(self, request:WowApiPowerTypeRequest.WowApiPowerTypeRequest):        
        request.endpoint = "/data/wow/power-type/%s" % request.powerTypeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
#endregion

#region Profession
    def GetProfessionIndex(self, request:WowApiProfessionRequest.WowApiProfessionRequest):        
        request.endpoint = "/data/wow/profession/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetProfession(self, request:WowApiProfessionRequest.WowApiProfessionRequest):        
        request.endpoint = "/data/wow/profession/%s" % request.professionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetProfessionMedia(self, request:WowApiProfessionRequest.WowApiProfessionRequest):        
        request.endpoint = "/data/wow/media/profession/%s" % request.professionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetProfessionSkillTier(self, request:WowApiProfessionRequest.WowApiProfessionRequest):        
        request.endpoint = f"/data/wow/profession/{request.professionId}/skill-tier/{request.skillTierId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetProfessionRecipe(self, request:WowApiProfessionRequest.WowApiProfessionRequest):        
        request.endpoint = "/data/wow/recipe/%s" % request.recipeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetProfessionRecipeMedia(self, request:WowApiProfessionRequest.WowApiProfessionRequest):        
        request.endpoint = "/data/wow/media/recipe/%s" % request.professionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
#endregion

#Pvp Season
    def GetPvpSeasonIndex(self, request:WowApiPvpSeasonRequest.WowApiPvpSeasonRequest):        
        request.endpoint = "/data/wow/pvp-season/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPvpSeason(self, request:WowApiPvpSeasonRequest.WowApiPvpSeasonRequest):        
        request.endpoint = "/data/wow/pvp-season/%s" % request.pvpSeasonId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetPvpLeaderboardIndex(self, request:WowApiPvpSeasonRequest.WowApiPvpSeasonRequest):        
        request.endpoint = f"/data/wow/pvp-season/{request.pvpSeasonId}/pvp-leaderboard/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPvpLeaderboard(self, request:WowApiPvpSeasonRequest.WowApiPvpSeasonRequest):        
        request.endpoint = f"/data/wow/pvp-season/{request.pvpSeasonId}/pvp-leaderboard/{request.pvpBracket}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response  

    def GetPvpRewardIndex(self, request:WowApiPvpSeasonRequest.WowApiPvpSeasonRequest):        
        request.endpoint = f"/data/wow/pvp-season/{request.pvpSeasonId}/pvp-reward/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response      
#endregion

#region Pvp Tier
    def GetPvpTierIndex(self, request:WowApiPvpTierRequest.WowApiPvpTierRequest):        
        request.endpoint = "/data/wow/pvp-tier/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response
    
    def GetPvpTier(self, request:WowApiPvpTierRequest.WowApiPvpTierRequest):        
        request.endpoint = "/data/wow/pvp-tier/%s" % request.pvpTierId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetPvpTierMedia(self, request:WowApiPvpTierRequest.WowApiPvpTierRequest):        
        request.endpoint = "/data/wow/media/pvp-tier/%s" % request.pvpTierId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Quest
    def GetQuestIndex(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetQuest(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/%s" % request.questId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetQuestCategoryIndex(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/category/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    

    def GetQuestCategory(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/category/%s" % request.questCategoryId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetQuestAreaIndex(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/area/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetQuestArea(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/area/%s" % request.questAreaId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetQuestTypeIndex(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/type/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetQuestType(self, request:WowApiQuestRequest.WowApiQuestRequest):        
        request.endpoint = "/data/wow/quest/type/%s" % request.questTypeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Realm
    def GetRealmIndex(self, request:WowApiRealmRequest.WowApiRealmRequest):        
        request.endpoint = "/data/wow/realm/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetRealm(self, request:WowApiRealmRequest.WowApiRealmRequest):        
        request.endpoint = "/data/wow/realm/%s" % request.realmSlug if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetRealmIndex(self, request:WowApiRealmRequest.WowApiRealmRequest):        
        request.endpoint = "/data/wow/search/realm" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Region
    def GetRegionIndex(self, request:WowApiRegionRequest.WowApiRegionRequest):        
        request.endpoint = "/data/wow/region/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetRegion(self, request:WowApiRegionRequest.WowApiRegionRequest):        
        request.endpoint = "/data/wow/region/%s" % request.regionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Reputation
    def GetReputationFactionIndex(self, request:WowApiReputationRequest.WowApiReputationRequest):        
        request.endpoint = "/data/wow/reputation-faction/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetReputationFaction(self, request:WowApiReputationRequest.WowApiReputationRequest):        
        request.endpoint = "/data/wow/reputation-faction/%s" % request.reputationFactionId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        

    def GetReputationTierIndex(self, request:WowApiReputationRequest.WowApiReputationRequest):        
        request.endpoint = "/data/wow/reputation-tiers/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    

    def GetReputationTier(self, request:WowApiReputationRequest.WowApiReputationRequest):        
        request.endpoint = "/data/wow/reputation-tiers/%s" % request.reputationTierId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
#endregion

#region Spell
    def GetSpell(self, request:WowApiSpellRequest.WowApiSpellRequest):        
        request.endpoint = "/data/wow/spell/%s" % request.spellId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    
    
    def GetSpell(self, request:WowApiSpellRequest.WowApiSpellRequest):        
        request.endpoint = "/data/wow/media/spell/%s" % request.spellId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
    
    def GetSpell(self, request:WowApiSpellRequest.WowApiSpellRequest):        
        request.endpoint = "/data/wow/search/spell" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response        
#endregion

#region Talent
    def GetTalentTreeIndex(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = "/data/wow/talent-tree/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response    

    def GetTalentTree(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = f"/data/wow/talent-tree/{request.talentTreeId}/playable-specialization/{request.specId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response     

    def GetTalentTreeNode(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = f"/data/wow/talent-tree/{request.talentTreeId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response  

    def GetTalentIndex(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = "/data/wow/talent/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                   
    
    def GetTalent(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = f"/data/wow/talent/{request.talentId}" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response         
    
    def GetPvpTalentIndex(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = "/data/wow/pvp-talent/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response         
    
    def GetPvpTalent(self, request:WowApiTalentRequest.WowApiTalentRequest):        
        request.endpoint = "/data/wow/pvp-talent/%s" % request.pvpTalentId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response             
#endregion

#region TechTalent
    def GetTechTalentTreeIndex(self, request:WowApiTechTalentRequest.WowApiTechTalentRequest):        
        request.endpoint = "/data/wow/tech-talent-tree/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response         
    
    def GetTechTalentTree(self, request:WowApiTechTalentRequest.WowApiTechTalentRequest):        
        request.endpoint = "/data/wow/tech-talent-tree/%s" % request.techTalentTreeId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response

    def GetTechTalentIndex(self, request:WowApiTechTalentRequest.WowApiTechTalentRequest):        
        request.endpoint = "/data/wow/tech-talent/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response         
    
    def GetTechTalent(self, request:WowApiTechTalentRequest.WowApiTechTalentRequest):        
        request.endpoint = "/data/wow/tech-talent/%s" % request.techTalentId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                 
    
    def GetTechTalentMedia(self, request:WowApiTechTalentRequest.WowApiTechTalentRequest):        
        request.endpoint = "/data/wow/media/tech-talent/%s" % request.techTalentId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response                     
#endregion

#region Title
    def GetTitleIndex(self, request:WowApiTitleRequest.WowApiTitleRequest):        
        request.endpoint = "/data/wow/title/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response         
    
    def GetTitle(self, request:WowApiTitleRequest.WowApiTitleRequest):        
        request.endpoint = "/data/wow/title/%s" % request.titleId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response         
#endregion

#region Toy
    def GetToyIndex(self, request:WowApiToyRequest.WowApiToyRequest):        
        request.endpoint = "/data/wow/toy/index" if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response  
    
    def GetToy(self, request:WowApiToyRequest.WowApiToyRequest):        
        request.endpoint = "/data/wow/toy/%s" % request.toyId if request.endpoint is None else request.endpoint
        response = self.ApiInvoker(request)
        return response      
#endregion

#region Wow Token
    def GetWowTokenIndex(self, request:WowApiWowTokenRequest.WowApiWowTokenRequest):        
        request.endpoint = "/data/wow/token/index"
        tokenPriceResponse = self.ApiInvoker(request)        
        return tokenPriceResponse.response["price"] / 10000 if tokenPriceResponse.success else tokenPriceResponse.errorMessage
    
    def GetWowTokenIndexChina(self, request:WowApiWowTokenRequest.WowApiWowTokenChinaRequest):        
        request.endpoint = "/data/wow/token/index"
        tokenPriceResponse = self.ApiInvoker(request)        
        return tokenPriceResponse.response["price"] / 10000 if tokenPriceResponse.success else tokenPriceResponse.errorMessage
#endregion    