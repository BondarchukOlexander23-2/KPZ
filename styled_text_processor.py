from html_element_processor import HtmlElementProcessor


class StyledTextProcessor(HtmlElementProcessor):
    def on_text_rendered(self, element):
        text = element.get('text', '')
        transformed = text.upper() if element.get('style', '').find('bold') != -1 else text
        print(f"[StyledText] {transformed}")
