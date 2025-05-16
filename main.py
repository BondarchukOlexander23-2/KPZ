from analytics_processor import AnalyticsProcessor
from debug_element_processor import DebugElementProcessor
from styled_text_processor import StyledTextProcessor


if __name__ == "__main__":
    element1 = {
        "tag": "div",
        "text": "Привіт",
        "class": ["main", "container"],
        "style": "color: red; font-weight: bold;"
    }

    element2 = {
        "tag": "p",
        "text": "Це абзац",
        "style": "font-style: italic;"
    }

    print("\n--- StyledTextProcessor ---")
    processor1 = StyledTextProcessor()
    processor1.process_element(element1)

    print("\n--- DebugElementProcessor ---")
    processor2 = DebugElementProcessor()
    processor2.process_element(element2)

    print("\n--- AnalyticsProcessor ---")
    processor3 = AnalyticsProcessor()
    processor3.process_element(element1)
    processor3.process_element(element2)
    processor3.report()
