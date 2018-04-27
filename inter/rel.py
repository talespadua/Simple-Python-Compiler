from symbols.array import Array
from symbols.type import Type
from .logical import Logical


class Rel(Logical):
    def __init__(self, token, x1, x2):
        super().__init__(token, x1, x2)

    def check(self, p1, p2):
        if isinstance(p1, Array) or isinstance(p2, Array):
            return None
        elif p1 == p2:
            return Type.bool_
        else:
            return None

    def jumping(self, t, f):
        a = self.expr1.reduce()
        b = self.expr2.reduce()
        test = '{} {} {}'.format(str(a), str(self.op), str(b))
        self.emitjumps(test, t, f)
