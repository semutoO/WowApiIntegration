from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiQuestRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, questId = None, questCategoryId = None, questAreaId = None, questTypeId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.questId = questId
        self.questCategoryId = questCategoryId
        self.questAreaId = questAreaId
        self.questTypeId = questTypeId