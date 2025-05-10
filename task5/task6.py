from light_element_node import LightElementNode, DisplayType, ClosingType
from light_text_node import LightTextNode


def convert_text_to_html(text):
    lines = text.strip().split('\n')
    root = LightElementNode("div").add_class("document")

    for i, line in enumerate(lines):
        if i == 0:
            root.add_child(LightElementNode("h1").add_text(line))
        elif line.startswith(' '):
            root.add_child(LightElementNode("blockquote").add_text(line.strip()))
        elif len(line) < 20:
            root.add_child(LightElementNode("h2").add_text(line))
        else:
            root.add_child(LightElementNode("p").add_text(line))

    return root


def calculate_memory_usage(element):
    розмір_елемента = 100

    if isinstance(element, LightTextNode):
        return розмір_елемента + len(element.text) * 2

    памʼять = розмір_елемента
    памʼять += len(element.tag_name) * 2

    for css_class in element.css_classes:
        памʼять += len(css_class) * 2 + 8

    for name, value in element.attributes.items():
        памʼять += (len(name) + len(value)) * 2 + 16

    for child in element.children:
        памʼять += calculate_memory_usage(child)

    return памʼять


def main():
    try:
        with open('romeo_and_juliet.txt', 'r', encoding='utf-8') as file:
            romeo_and_juliet_text = file.read()
    except FileNotFoundError:
        print("Помилка: файл 'romeo_and_juliet.txt' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return

    print(f"Файл 'romeo_and_juliet.txt' успішно прочитано, обробка {len(romeo_and_juliet_text)} символів...")

    html_tree = convert_text_to_html(romeo_and_juliet_text)

    print("Згенерована HTML-структура:")
    print(html_tree.get_outer_html())

    try:
        with open('romeo_and_juliet.html', 'w', encoding='utf-8') as file:
            file.write(html_tree.get_outer_html())
        print("\nHTML успішно збережено у 'romeo_and_juliet.html'")
    except Exception as e:
        print(f"\nПомилка збереження HTML у файл: {e}")

    memory_usage = calculate_memory_usage(html_tree)
    print(f"\nОрієнтовне використання памʼяті: {memory_usage} байт ({memory_usage / 1024:.2f} КБ)")

    print("\nТестування окремих методів:")
    print(f"Кількість дочірніх елементів кореня: {html_tree.get_child_count()}")

    print("\ninner_html кореневого елемента:")
    print(html_tree.get_inner_html())


if __name__ == "__main__":
    main()
