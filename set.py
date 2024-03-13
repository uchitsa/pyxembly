from lxml.html import parse

from xembly.base import Xembly


class Set:
    def __init__(self, value):
        self.value = value

    def exec(self, _, cursor):
        for node in cursor:
            node.content = parse(self.value.text)
            Xembly.log.info(f"node \"{node.name}\" text content set")
        return cursor
