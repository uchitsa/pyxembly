import logging


class Attr:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def exec(self, _, cursor):
        for node in cursor:
            node[self.name] = self.value
            logging.info(f'attribute "{self.name}" set for node "{node.name}"')
        return cursor
