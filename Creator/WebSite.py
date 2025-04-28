from Creator.SubscriptionCreator import SubscriptionCreator
from Subscriptions.DomesticSubscription import DomesticSubscription
from Subscriptions.EducationalSubscription import EducationalSubscription
from Subscriptions.PremiumSubscription import PremiumSubscription

class WebSite(SubscriptionCreator):
    def create_subscription(self, subscription_type):
        print("Creating subscription via WebSite...")
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type!")