from abc import ABC, abstractmethod

class Subscription(ABC):
    @abstractmethod
    def get_monthly_fee(self):
        pass

    @abstractmethod
    def get_min_period(self):  # у місяцях
        pass

    @abstractmethod
    def get_channels(self):
        pass

    @abstractmethod
    def get_features(self):
        pass
