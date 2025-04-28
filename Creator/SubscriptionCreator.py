from abc import ABC, abstractmethod

class SubscriptionCreator(ABC):
    @abstractmethod
    def create_subscription(self, subscription_type):
        pass