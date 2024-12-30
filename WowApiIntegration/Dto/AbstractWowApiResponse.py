class AbstractWowApiResponse:
    success = True,
    errorMessage = None
    response = None

    def __init__(self, success, errorMessage, response):
        self.success = success
        self.errorMessage = errorMessage
        self.response = response