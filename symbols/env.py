class Env:

    def __init__(self, n):
        self.table = []
        self.prev = n

    def put(self, w, i):
        self.table.append((w, i))

    def get(self, w):
        e = self
        while e is not None:
            e = e.prev
            found = dict(e.table)[w]
            if found is not None:
                return found
        return None
