from .id import Id
from .token import Token


class Env:

    def __init__(self, n):
        self.table = []
        self.prev = n

    def put(self, w, i):
        self.table.put(w, i)

    def get(self, w):
        e = self
        while e is not None:
            e = e.prev
            found = e.table.get(w)
            if found is not None:
                return found
        return None