from symbols.type import Type
from symbols.array import Array
from .stmt import Stmt


class SetElem(Stmt):

    def __init__(self, x, y):
        # super().__init__()
        self.array = x.array
        self.index = x.index
        self.expr = y

        if self.check(x.type_, self.expr.type_) is None:
            self.error("type error")

    def check(self, p1, p2):
        if isinstance(p1, Array) and isinstance(p2, Array):
            return None
        elif p1 == p2:
            return p2
        elif Type.numeric(p1) and Type.numeric(p2):
            return p2
        else:
            return None

    def gen(self, b, a):
        s1 = str(self.index.reduce())
        s2 = str(self.expr.reduce())
        self.emit("{} [{}] = {}".format(str(self.array, s1, s2)))
