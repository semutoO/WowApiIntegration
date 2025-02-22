from WowApiIntegration.Dto import AbstractWowApiRequest

#Searches should let you query an endpoint based on any property returned in their response
#Adding extra parameters to the query string can cause it to return empty results 
#Item Searches doesn't support region
#Connected Realm Searches doesn't support locale

#Use searchDictionary to specify a key/value pair that will add url params in the invoker as key=value
#Item Search Example: { "id" : "[1,1000]" }
#Connected Realm Example: { "realms.slug" : "moonrunner" }
class AbstractWowApiSearchRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, orderBy = None, page = 1, pageSize = 50, endpoint = None, region=None, namespace="dynamic-us", locale=None, searchDictionary:dict = None):
        super().__init__(region, namespace, locale, endpoint)                        
        self.region = region if region is not None else None
        self.locale = locale if locale is not None else None 
        self.orderby = orderBy
        self._page = page
        self._pageSize = pageSize
        self.searchDictionary:dict = searchDictionary