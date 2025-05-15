from breadth_first_iterator import BreadthFirstIterator
from depth_first_iterator import DepthFirstIterator
from html_bread_first_iterator import HtmlBreadthFirstIterator
from html_depth_first_iterator import HtmlDepthFirstIterator




class IterableDocument:
    def __init__(self, content, is_html=False):
        self._content = content
        self._is_html = is_html

    def create_depth_iterator(self):
        if self._is_html:
            return HtmlDepthFirstIterator(self._content)
        else:
            return DepthFirstIterator(self._content)

    def create_breadth_iterator(self):
        if self._is_html:
            return HtmlBreadthFirstIterator(self._content)
        else:
            return BreadthFirstIterator(self._content)