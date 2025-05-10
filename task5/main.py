from light_element_node import LightElementNode
from light_image_node import LightImageNode
from image_strategy_context import ImageStrategyContext


def main():

    print("===== Тестування LightImageNode зі стратегічним шаблоном =====\n")

    gallery = LightElementNode("div").add_class("image-gallery")

    local_image = LightImageNode("Тест локального зображення", "test.jpg")
    local_container = LightElementNode("div").add_class("image-container")
    local_container.add_child(LightElementNode("h3").add_text("Локальне зображення"))
    local_container.add_child(local_image)
    gallery.add_child(local_container)

    network_image = LightImageNode("Тест мережевого зображення", "https://example.com/image.jpg")
    network_container = LightElementNode("div").add_class("image-container")
    network_container.add_child(LightElementNode("h3").add_text("Мережеве зображення"))
    network_container.add_child(network_image)
    gallery.add_child(network_container)

    missing_image = LightImageNode("Тест відсутнього зображення", "non_existent_image.jpg")
    missing_container = LightElementNode("div").add_class("image-container")
    missing_container.add_child(LightElementNode("h3").add_text("Відсутнє зображення"))
    missing_container.add_child(missing_image)
    gallery.add_child(missing_container)

    invalid_url_image = LightImageNode("Тест некоректного URL", "https://this-is-not-a-valid-domain-for-sure.xyz/image.jpg")
    invalid_url_container = LightElementNode("div").add_class("image-container")
    invalid_url_container.add_child(LightElementNode("h3").add_text("Некоректний URL"))
    invalid_url_container.add_child(invalid_url_image)
    gallery.add_child(invalid_url_container)

    print("Згенерований HTML:")
    print(gallery.get_outer_html())

    print("\n\nТестування вибору стратегії напряму:")
    strategy_context = ImageStrategyContext()

    test_sources = [
        "local_file.jpg",
        "/absolute/path/image.png",
        "https://example.com/image.jpg",
        "http://test.com/icon.gif"
    ]

    for src in test_sources:
        strategy = strategy_context.get_strategy(src)
        print(f"Джерело: {src} => Стратегія: {strategy.get_strategy_name()}")

    print("\n===== Демонстрацію завершено =====")


if __name__ == "__main__":
    main()
