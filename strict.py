from base import Base


class Strict(Base):
    def __init__(self, count):
        self.count = int(count)

    def exec(self, _, cursor):
        if len(cursor) != self.count:
            raise Exception(f"there are {len(cursor)} nodes, while {self.count} expected")
        return cursor
