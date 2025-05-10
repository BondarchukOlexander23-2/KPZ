from file_system_image_strategy import FileSystemImageStrategy
from network_image_strategy import NetworkImageStrategy


class ImageStrategyContext:

    def __init__(self):
        self.file_strategy = FileSystemImageStrategy()
        self.network_strategy = NetworkImageStrategy()

    def get_strategy(self, href):
        if href.startswith(('http://', 'https://', 'ftp://')):
            return self.network_strategy
        else:
            return self.file_strategy

    def load_image(self, href):
        strategy = self.get_strategy(href)
        success, data = strategy.load_image(href)
        return success, data, strategy.get_strategy_name()