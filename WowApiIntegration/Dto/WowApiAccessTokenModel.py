#Example Response {"access_token": "foobar", "token_type": "bearer", "expires_in": 86399, "scope": "example.scope"}
import datetime

class WowApiAccessTokenModel:   
    def __init__(self, accessToken, expiresTimeInSeconds, scope, tokenType = "bearer"):
        self.accessToken = accessToken
        self.expirationDate = datetime.timedelta(0,expiresTimeInSeconds)
        self.scope = scope
        self.tokenType = tokenType

    def IsTokenExpired(self):
        return self.expirationDate == None or self.expirationDate < datetime.datetime.now