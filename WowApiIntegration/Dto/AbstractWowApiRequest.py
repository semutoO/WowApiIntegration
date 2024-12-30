class AbstractWowApiRequest:
    region = "us"
    namespace = "dynamic-us"
    locale = "en_US"
    endpoint = None

    def __init__(self, region, namespace, locale, endpoint):
        self.region = region
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint