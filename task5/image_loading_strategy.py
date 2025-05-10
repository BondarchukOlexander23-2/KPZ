from abc import ABC, abstractmethod


class ImageLoadingStrategy(ABC):

    @abstractmethod
    def load_image(self, href):
        pass

    @abstractmethod
    def get_strategy_name(self):
        pass