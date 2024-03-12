import logging
from lxml import etree


class AddIf:
    def __init__(self, name):
        self.name = name

    def exec(self, dom, cursor):
        after = []
        for node in cursor:
            if not any(e for e in node.iterchildren() if e.tag == self.name):
                child = etree.Element(self.name)
                node.append(child)
                after.append(child)
                logging.info(f'node "{self.name}" added to "{node.tag}"')
            else:
                after.append(node)
        return after
