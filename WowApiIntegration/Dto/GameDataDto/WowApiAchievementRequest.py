from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiAchievementRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    achievementId = None
    achievementCategoryId = None

    def __init__(self, endpoint, achievementId=None, achievementCategoryId=None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.achievementId = achievementId
        self.achievementCategoryId = achievementCategoryId
