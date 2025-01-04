from WowApiIntegration.Dto import AbstractWowApiRequest


class WowApiJournalRequest(AbstractWowApiRequest.AbstractWowApiRequest):
    def __init__(self, endpoint = None, journalExpansionId = None, journalEncounterId = None, journalInstanceId = None, region="us", namespace="static-us", locale="en_US"):
        super().__init__(region, namespace, locale, endpoint)
        self.journalExpansionId = journalExpansionId
        self.journalEncounterId = journalEncounterId
        self.journalInstanceId = journalInstanceId