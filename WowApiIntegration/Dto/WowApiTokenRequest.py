class WowApiTokenRequest:
    region = "us"
    namespace = "dynamic-us"
    locale = "en_US"    

    def __init__(self, region, namespace, locale):
        self.region = region
        self.namespace = namespace
        self.locale = locale
