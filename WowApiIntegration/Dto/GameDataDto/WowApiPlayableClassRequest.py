from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPlayableClassRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, classId = None, playableClassId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.classId = classId
        self.playableClassId = playableClassId
