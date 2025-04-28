from Subscriptions.Subscription import Subscription


class DomesticSubscription(Subscription):
    def get_monthly_fee(self):
        return 9.99

    def get_min_period(self):
        return 6

    def get_channels(self):
        return ["Sport, Films, News"]

    def get_features(self):
        return "Standard Definition, 2 devices"
