from collections import deque

from html_iterator import HtmlIterator


class HtmlBreadthFirstIterator(HtmlIterator):
    """
    Ітератор для обходу HTML-документа в ширину
    """
    def _collect_elements(self):
        queue = deque([self._soup])

        while queue:
            element = queue.popleft()
            self._elements.append(element)

            if hasattr(element, 'contents'):
                for child in element.contents:
                    queue.append(child)