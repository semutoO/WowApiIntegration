from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiPlayableClassRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    classId = None
    playableClassId = None

    def __init__(self, endpoint, classId = None, playableClassId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.classId = classId
        self.playableClassId = playableClassId
