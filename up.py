import sys

sys.path.append('../pyxembly')


class Up:
    @staticmethod
    def exec(_, cursor):
        after = []
        for node in cursor:
            after.append(node.getparent())
        return after
