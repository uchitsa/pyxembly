import sys

sys.path.append('../pyxembly')


class Up:
    def exec(self, _, cursor):
        after = []
        for node in cursor:
            after.append(node.getparent())
        return after
