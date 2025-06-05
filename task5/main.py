from light_element_node import LightElementNode, DisplayType, ClosingType


def button_click_handler(element, event_data):
    print(f"Button clicked! Text: '{element.children[0].text}'")
    if event_data:
        print(f"Event data: {event_data}")


def mouse_over_handler(element, event_data):
    print(f"Mouse over '{element.tag_name}' element with class '{' '.join(element.css_classes)}'")


def form_submit_handler(element, event_data):
    print(f"Form submitted: {event_data}")


def create_interactive_form():

    form = LightElementNode("form").add_class("user-form")
    form.add_event_listener("submit", form_submit_handler)

    form.add_child(LightElementNode("h2").add_text("Інтерактивна форма"))

    name_container = LightElementNode("div").add_class("form-group")
    name_label = LightElementNode("label", display_type=DisplayType.BLOCK)
    name_label.add_attribute("for", "username").add_text("Ім'я користувача:")
    name_input = LightElementNode("input", closing_type=ClosingType.SELF_CLOSING)
    name_input.add_attribute("type", "text")
    name_input.add_attribute("id", "username")
    name_input.add_attribute("placeholder", "Введіть ваше ім'я")
    name_input.add_event_listener("focus", lambda e, d: print("Name field focused"))

    name_container.add_child(name_label)
    name_container.add_child(name_input)
    form.add_child(name_container)

    email_container = LightElementNode("div").add_class("form-group")
    email_label = LightElementNode("label", display_type=DisplayType.BLOCK)
    email_label.add_attribute("for", "email").add_text("Email:")
    email_input = LightElementNode("input", closing_type=ClosingType.SELF_CLOSING)
    email_input.add_attribute("type", "email")
    email_input.add_attribute("id", "email")
    email_input.add_attribute("placeholder", "Введіть ваш email")
    email_input.add_event_listener("change", lambda e, d: print("Email field changed"))

    email_container.add_child(email_label)
    email_container.add_child(email_input)
    form.add_child(email_container)

    button = LightElementNode("button")
    button.add_class("btn").add_class("primary")
    button.add_attribute("type", "submit")
    button.add_text("Відправити")
    button.add_event_listener("click", button_click_handler)
    button.add_event_listener("mouseover", mouse_over_handler)

    form.add_child(button)

    return form


def create_interactive_card():

    card = LightElementNode("div").add_class("user-card").add_class("interactive")

    card.add_event_listener("mouseover", lambda e, d: print("Card hovered!"))
    card.add_event_listener("mouseout", lambda e, d: print("Mouse left the card"))

    header = LightElementNode("header").add_class("card-header")
    header.add_child(LightElementNode("h2").add_text("Інтерактивна картка"))
    card.add_child(header)

    content = LightElementNode("div").add_class("card-content")

    avatar = LightElementNode("img", display_type=DisplayType.INLINE,
                              closing_type=ClosingType.SELF_CLOSING)
    avatar.add_attribute("src", "avatar.jpg")
    avatar.add_attribute("alt", "Аватар користувача")
    avatar.add_class("avatar")
    avatar.add_event_listener("click", lambda e, d: print("Avatar image clicked!"))
    content.add_child(avatar)

    info = LightElementNode("div").add_class("user-info")

    name_container = LightElementNode("div").add_class("info-row")
    name_container.add_child(LightElementNode("span").add_class("label").add_text("Ім'я:"))
    user_name = LightElementNode("span").add_text("Іван Петренко")
    user_name.add_event_listener("click", lambda e, d: print("User name clicked!"))
    name_container.add_child(user_name)
    info.add_child(name_container)

    email_container = LightElementNode("div").add_class("info-row")
    email_container.add_child(LightElementNode("span").add_class("label").add_text("Email:"))
    email_container.add_child(LightElementNode("span").add_text("ivan@example.com"))
    info.add_child(email_container)

    content.add_child(info)
    card.add_child(content)

    footer = LightElementNode("footer").add_class("card-footer")
    edit_button = LightElementNode("button").add_class("btn").add_class("primary")
    edit_button.add_text("Редагувати профіль")
    edit_button.add_event_listener("click", button_click_handler)
    footer.add_child(edit_button)
    card.add_child(footer)

    return card


def main():

    print("===== Демонстрація роботи EventListener у LightHTML =====\n")

    form = create_interactive_form()
    card = create_interactive_card()

    print("\n1. HTML структура інтерактивної форми:")
    print(form.get_outer_html())

    print("\n2. HTML структура інтерактивної картки:")
    print(card.get_outer_html())

    print("\n3. Демонстрація спрацювання подій:")
    print("\n--- Симуляція натискання кнопки форми ---")
    form.children[-1].trigger_event("click", {"button_id": 1})

    print("\n--- Симуляція наведення курсора на кнопку ---")
    form.children[-1].trigger_event("mouseover")

    print("\n--- Симуляція відправки форми ---")
    form.trigger_event("submit", {"username": "user123", "email": "user@example.com"})

    print("\n--- Симуляція кліку на аватар користувача ---")
    avatar_element = card.children[1].children[0]
    avatar_element.trigger_event("click")

    print("\n--- Симуляція наведення на картку ---")
    card.trigger_event("mouseover")

    print("\n--- Симуляція кліку на кнопку редагування профілю ---")
    edit_button = card.children[2].children[0]
    edit_button.trigger_event("click", {"user_id": 42})

    print("\n4. Демонстрація видалення слухача подій:")
    print("--- До видалення ---")
    card.trigger_event("mouseover")

    print("\n--- Видалення всіх слухачів події 'mouseover' ---")
    card.remove_event_listener("mouseover")

    print("--- Після видалення ---")
    result = card.trigger_event("mouseover")
    print(f"Подія спрацювала: {result}")  

    print("\n===== Демонстрація завершена =====")


if __name__ == "__main__":
    main()