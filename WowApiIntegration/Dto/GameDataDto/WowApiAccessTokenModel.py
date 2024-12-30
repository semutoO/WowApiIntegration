#Example {"access_token": "foobar", "token_type": "bearer", "expires_in": 86399, "scope": "example.scope"}
import datetime

class WowApiAccessTokenModel:
    accessToken = None
    tokenType = "bearer"
    expirationDate: datetime = None
    scope = None

    def __init__(self, accessToken, tokenType, expiresTimeInSeconds, scope):
        self.accessToken = accessToken
        self.tokenType = tokenType
        self.expirationDate = datetime.timedelta(0,expiresTimeInSeconds)
        self.scope = scope

    def IsTokenExpired(self):
        return self.expirationDate == None or self.expirationDate < datetime.datetime.now