class WowApiCredentialModel:
    clientId = None
    clientSecret = None

    def __init__(self, clientId, clientSecret):
        self.clientId = clientId
        self.clientSecret = clientSecret