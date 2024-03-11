import logging
from lxml import etree

class Xembler:
    def __init__(self, dirs):
        self.dirs = dirs

    def apply(self, xml):
        dom = etree.fromstring(xml)
        cursor = [dom]
        for dir in self.dirs:
            cursor = dir.exec(dom, cursor)
            logging.info(f"Applied: {dir}")
        logging.info(f"{len(self.dirs)} directive(s) applied")
        return dom

