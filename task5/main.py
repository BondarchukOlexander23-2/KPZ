from light_element_node import LightElementNode, DisplayType, ClosingType
from light_text_node import LightTextNode


def create_table_example():

    table = LightElementNode("table").add_class("data-table").add_class("bordered")

    # Додаємо заголовок таблиці
    thead = LightElementNode("thead")
    header_row = LightElementNode("tr")

    # Додаємо заголовки колонок
    header_row.add_child(LightElementNode("th").add_text("№"))
    header_row.add_child(LightElementNode("th").add_text("Назва продукту"))
    header_row.add_child(LightElementNode("th").add_text("Ціна"))
    header_row.add_child(LightElementNode("th").add_text("Кількість"))

    thead.add_child(header_row)
    table.add_child(thead)

    # Додаємо тіло таблиці
    tbody = LightElementNode("tbody")

    # Перший рядок
    row1 = LightElementNode("tr")
    row1.add_child(LightElementNode("td").add_text("1"))
    row1.add_child(LightElementNode("td").add_text("Ноутбук"))
    row1.add_child(LightElementNode("td").add_text("25000 грн"))
    row1.add_child(LightElementNode("td").add_text("2"))
    tbody.add_child(row1)

    # Другий рядок
    row2 = LightElementNode("tr").add_class("highlighted")
    row2.add_child(LightElementNode("td").add_text("2"))
    row2.add_child(LightElementNode("td").add_text("Смартфон"))
    row2.add_child(LightElementNode("td").add_text("12000 грн"))
    row2.add_child(LightElementNode("td").add_text("5"))
    tbody.add_child(row2)

    # Третій рядок
    row3 = LightElementNode("tr")
    row3.add_child(LightElementNode("td").add_text("3"))
    row3.add_child(LightElementNode("td").add_text("Навушники"))
    row3.add_child(LightElementNode("td").add_text("1500 грн"))
    row3.add_child(LightElementNode("td").add_text("10"))
    tbody.add_child(row3)

    table.add_child(tbody)

    return table


def create_user_card_example():

    card = LightElementNode("div").add_class("user-card").add_class("shadow")

    header = LightElementNode("header").add_class("card-header")
    header.add_child(LightElementNode("h2").add_text("Профіль користувача"))
    card.add_child(header)

    content = LightElementNode("div").add_class("card-content")

    avatar = LightElementNode("img", display_type=DisplayType.INLINE,
                              closing_type=ClosingType.SELF_CLOSING)
    avatar.add_attribute("src", "avatar.jpg")
    avatar.add_attribute("alt", "Аватар користувача")
    avatar.add_class("avatar")
    content.add_child(avatar)

    info = LightElementNode("div").add_class("user-info")

    name_container = LightElementNode("div").add_class("info-row")
    name_container.add_child(LightElementNode("span").add_class("label").add_text("Ім'я:"))
    name_container.add_child(LightElementNode("span").add_text("Іван Петренко"))
    info.add_child(name_container)

    email_container = LightElementNode("div").add_class("info-row")
    email_container.add_child(LightElementNode("span").add_class("label").add_text("Email:"))
    email_container.add_child(LightElementNode("span").add_text("ivan@example.com"))
    info.add_child(email_container)

    phone_container = LightElementNode("div").add_class("info-row")
    phone_container.add_child(LightElementNode("span").add_class("label").add_text("Телефон:"))
    phone_container.add_child(LightElementNode("span").add_text("+380991234567"))
    info.add_child(phone_container)

    content.add_child(info)
    card.add_child(content)

    footer = LightElementNode("footer").add_class("card-footer")
    footer.add_child(
        LightElementNode("button")
        .add_class("btn")
        .add_class("primary")
        .add_text("Редагувати профіль")
    )
    card.add_child(footer)

    return card


def main():

    print("Приклад таблиці")
    table = create_table_example()
    print(table.get_outer_html())

    print("\n\nПриклад картки користувача")
    user_card = create_user_card_example()
    print(user_card.get_outer_html())

    print("\n\nТестування окремих функцій")
    div = LightElementNode("div").add_class("container")
    div.add_child(LightElementNode("p").add_text("Це перший параграф"))
    div.add_child(LightElementNode("p").add_text("Це другий параграф"))

    print("outer_html для div:")
    print(div.get_outer_html())

    print("\ninner_html для div:")
    print(div.get_inner_html())

    print(f"\nКількість дочірніх елементів div: {div.get_child_count()}")


if __name__ == "__main__":
    main()