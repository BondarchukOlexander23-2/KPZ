from command import OnCreatedCommand, OnInsertedCommand, OnRemovedCommand, OnTextRenderedCommand, OnStylesAppliedCommand
from elements import SmartElement
from document import SmartDocument

doc = SmartDocument()

div = SmartElement("div", text="Привіт, світ!", attributes={"style": "color: red;"})
div.set_hook("on_created", OnCreatedCommand())
div.set_hook("on_inserted", OnInsertedCommand())
div.set_hook("on_removed", OnRemovedCommand())
div.set_hook("on_text_rendered", OnTextRenderedCommand())
div.set_hook("on_styles_applied", OnStylesAppliedCommand())

doc.add_element(div)

doc.render()

doc.remove_element(div)
