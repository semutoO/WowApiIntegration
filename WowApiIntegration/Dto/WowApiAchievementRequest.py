class WowApiAchievementRequest:
    region = "us"
    realmSlug = None
    characterName = None
    namespace = "profile-us"
    locale = "en_US"
    endpoint = None

    def __init__(self, region, realmSlug, charName, namespace, locale, endpoint):
        self.region = region
        self.realmSlug = realmSlug
        self.characterName = charName
        self.namespace = namespace
        self.locale = locale
        self.endpoint = endpoint
