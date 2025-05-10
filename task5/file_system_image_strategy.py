from image_loading_strategy import ImageLoadingStrategy
import os
import base64
import mimetypes

class FileSystemImageStrategy(ImageLoadingStrategy):

    def load_image(self, href):
        try:
            if not os.path.exists(href):
                return False, f"File not found: {href}"

            with open(href, 'rb') as file:
                image_data = file.read()

            mime_type, _ = mimetypes.guess_type(href)
            if not mime_type:
                mime_type = 'image/png'

            base64_data = base64.b64encode(image_data).decode('utf-8')
            data_url = f"data:{mime_type};base64,{base64_data}"

            return True, data_url
        except Exception as e:
            return False, f"Error loading file: {e}"

    def get_strategy_name(self):
        return "FileSystem"