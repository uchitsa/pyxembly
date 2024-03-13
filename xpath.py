class Xpath:
    def __init__(self, path):
        self.path = path

    def exec(self, dom, cursor):
        if self.path.startswith('/'):
            after = dom.findall(self.path)
        else:
            after = []
            for node in cursor:
                after.extend(node.findall(self.path))
        return after
