class AbstractWowApiResponse:    
    def __init__(self, success = True, errorMessage = None, response = None):
        self.success = success
        self.errorMessage = errorMessage
        self.response = response