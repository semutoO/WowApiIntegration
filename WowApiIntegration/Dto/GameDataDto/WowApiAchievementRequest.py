from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiAchievementRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, achievementId=None, achievementCategoryId=None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)        
        self.achievementId = achievementId
        self.achievementCategoryId = achievementCategoryId