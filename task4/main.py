from elements import Element
from state import HiddenState, DisabledState, LoadingState, VisibleState

root = Element("div")
header = Element("h1", "Заголовок сторінки")
button = Element("button", "Натисни мене")
loader = Element("span")

root.add_child(header)
root.add_child(button)
root.add_child(loader)

print("=== Видимий стан ===")
root.render()

print("\n=== Кнопка неактивна ===")
button.set_state(DisabledState())
root.render()

print("\n=== Увесь контейнер приховано ===")
root.propagate_state(HiddenState())
root.render()

print("\n=== Завантаження тільки спана ===")
loader.set_state(LoadingState())
root.set_state(VisibleState())
root.render()
