class AbstractWowApiRequest:    
    def __init__(self, region = "us", namespace = "dynamic-us", locale="en_US", endpoint=None):
        self.region = region if region is not None else "us"
        self.namespace = namespace if namespace is not None else "dynamic-us"
        self.locale = locale if locale is not None else "en_US"
        self.endpoint = endpoint