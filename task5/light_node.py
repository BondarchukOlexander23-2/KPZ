from abc import ABC, abstractmethod

class LightNode(ABC):

    @abstractmethod
    def get_outer_html(self):
        pass

    @abstractmethod
    def get_inner_html(self):
        pass