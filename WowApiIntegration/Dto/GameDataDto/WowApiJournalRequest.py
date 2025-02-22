from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiJournalRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    journalExpansionId = None
    journalEncounterId = None
    journalInstanceId = None    

    def __init__(self, endpoint, journalExpansionId = None, journalEncounterId = None, journalInstanceId = None, region="us", namespace="static-us", locale="en_US"):
        self.region = region        
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
        self.journalExpansionId = journalExpansionId
        self.journalEncounterId = journalEncounterId
        self.journalInstanceId = journalInstanceId