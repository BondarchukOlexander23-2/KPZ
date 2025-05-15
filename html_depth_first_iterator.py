from html_iterator import HtmlIterator


class HtmlDepthFirstIterator(HtmlIterator):
    def _collect_elements(self):
        def collect_dfs(element):
            self._elements.append(element)
            if hasattr(element, 'contents'):
                for child in element.contents:
                    collect_dfs(child)

        collect_dfs(self._soup)