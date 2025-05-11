from extended_text_reader import SmartIterableTextReader
import re


class HtmlSearcher:
    """
    Клас для пошуку в HTML-документах, що використовує ітератори
    """
    def __init__(self, html_document):
        self._document = html_document

    def find_elements_by_tag(self, tag_name):
        results = []
        iterator = self._document.create_depth_iterator()

        while iterator.has_next():
            element = iterator.next()

            if hasattr(element, 'name') and element.name == tag_name:
                results.append(element)

        return results

    def find_elements_by_class(self, class_name):
        results = []
        iterator = self._document.create_depth_iterator()

        while iterator.has_next():
            element = iterator.next()

            if hasattr(element, 'attrs') and 'class' in element.attrs:
                if class_name in element.attrs['class']:
                    results.append(element)

        return results

    def find_text_by_pattern(self, pattern):
        results = []
        iterator = self._document.create_depth_iterator()
        regex = re.compile(pattern)

        while iterator.has_next():
            element = iterator.next()

            if isinstance(element, str) and element.strip():
                text = element.strip()
                if regex.search(text):
                    results.append(text)

        return results


def test_html_search():
    print("\n=== Тестування пошуку в HTML-документі ===")

    reader = SmartIterableTextReader()
    document = reader.create_iterable_document("test.html")

    searcher = HtmlSearcher(document)

    print("\nПошук за тегом 'p':")
    paragraphs = searcher.find_elements_by_tag('p')
    for p in paragraphs:
        print(f"- {p.text.strip()}")

    print("\nПошук за класом 'content':")
    content_elements = searcher.find_elements_by_class('content')
    for el in content_elements:
        print(f"- <{el.name}> з {len(el.contents)} дочірніми елементами")

    print("\nПошук тексту за шаблоном 'параграф':")
    text_matches = searcher.find_text_by_pattern(r'параграф')
    for text in text_matches:
        print(f"- {text}")


if __name__ == "__main__":
    with open("test.html", "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Тестова HTML-сторінка</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Заголовок сторінки</h1>
    <div class="content">
        <p>Перший параграф</p>
        <p>Другий параграф</p>
        <ul>
            <li>Пункт 1</li>
            <li>Пункт 2</li>
            <li>Пункт 3</li>
        </ul>
    </div>
    <footer>
        Підвал сторінки
    </footer>
</body>
</html>""")

    test_html_search()