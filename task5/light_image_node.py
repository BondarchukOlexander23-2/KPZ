from light_element_node import LightElementNode, DisplayType, ClosingType
from image_strategy_context import ImageStrategyContext


class LightImageNode(LightElementNode):
    def __init__(self, alt_text="", src=""):
        super().__init__("img", display_type=DisplayType.INLINE,
                         closing_type=ClosingType.SELF_CLOSING)

        self.strategy_context = ImageStrategyContext()

        if alt_text:
            self.add_attribute("alt", alt_text)

        if src:
            self.set_src(src)

    def set_src(self, href):
        success, src_data, strategy_name = self.strategy_context.load_image(href)

        if success:
            self.add_attribute("src", src_data)
            # Add a data attribute to show which strategy was used (for demonstration)
            self.add_attribute("data-loading-strategy", strategy_name)
        else:
            self.add_attribute("data-error", "true")
            self.add_attribute("data-error-message", src_data)
            self.add_attribute("src", "")

        return self