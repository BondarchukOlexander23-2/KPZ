from Subscriptions.Subscription import Subscription

class PremiumSubscription(Subscription):
    def get_monthly_fee(self):
        return 19.99

    def get_min_period(self):
        return 1

    def get_channels(self):
        return ["All channels", "Movies", "Series", "Documentaries"]

    def get_features(self):
        return "4K UHD, Unlimited devices, Offline download"