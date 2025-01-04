from WowApiIntegration.Dto import AbstractWowApiRequest

class WowApiSpellRequest(AbstractWowApiRequest.AbstractWowApiRequest):    
    def __init__(self, spellId = None, endpoint = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.spellId = spellId