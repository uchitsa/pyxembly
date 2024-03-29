import logging


class Remove:
    @staticmethod
    def exec(_, cursor):
        after = []
        for node in cursor:
            logging.info(f"node \"{node.name}\" removed")
            parent = node.parent
            node.remove()
            after.append(parent)
        return after
