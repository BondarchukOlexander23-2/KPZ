from image_loading_strategy import ImageLoadingStrategy
import urllib.request
import urllib.error


class NetworkImageStrategy(ImageLoadingStrategy):

    def load_image(self, href):
        try:
            request = urllib.request.Request(href, method="HEAD")
            with urllib.request.urlopen(request, timeout=5) as response:
                if response.getcode() == 200:
                    return True, href

            return False, f"Could not access URL: {href}"
        except urllib.error.URLError as e:
            return False, f"URL error: {e.reason}"
        except Exception as e:
            return False, f"Error accessing URL: {e}"

    def get_strategy_name(self):
        return "Network"