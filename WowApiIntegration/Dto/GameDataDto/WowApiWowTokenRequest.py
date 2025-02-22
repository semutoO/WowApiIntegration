from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiWowTokenRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, endpoint = None, region="us", namespace="dynamic-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)

class WowApiWowTokenChinaRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, region="cn", namespace="dynamic-cn", locale="zh_CN"):
        super().__init__(region, namespace, locale, endpoint)            