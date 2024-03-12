import logging
from lxml import etree

logging.basicConfig(level=logging.INFO)


class Add:
    def __init__(self, name):
        self.name = name

    def exec(self, dom, cursor):
        after = []
        for node in cursor:
            child = etree.Element(self.name)
            node.append(child)
            after.append(child)
            logging.info(f'node "{self.name}" added to "{node.tag}"')
        return after
