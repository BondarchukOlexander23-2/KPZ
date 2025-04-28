from Subscriptions.Subscription import Subscription

class EducationalSubscription(Subscription):
    def get_monthly_fee(self):
        return 5.99

    def get_min_period(self):
        return 3

    def get_channels(self):
        return ["Discovery", "National Geographic", "History"]

    def get_features(self):
        return "HD content, Educational material access"