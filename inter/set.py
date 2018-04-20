from symbols.type import Type
from .stmt import Stmt


class Set(Stmt):

    def __init__(self, i, x):
        # super().__init__()
        self.id = i
        self.expr = x
        if self.check(self.id.type_p, self.expr.type_p) is None:
            self.error("type error")

    def check(self, p1, p2):
        if Type.numeric(p1) and Type.numeric(p2):
            return p2
        elif p1 is Type._bool() and p2 is Type._bool():
            return p2
        else:
            return None

    def gen(self, b, a):
        self.emit("{} = {}".format(str(self.id), str(self.expr.gen())))
