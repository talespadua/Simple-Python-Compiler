from .op import Op
from symbols.type import Type


class Arith(Op):
    def __init__(self, token, x1, x2):
        super().__init__(token, None)
        self.expr1 = x1
        self.expr2 = x2
        self.type_ = Type.max(self.expr1.type, self.expr2.type)
        if type is None:
            self.error('Type Error')

    def gen(self):
        return self.__class__(self.op, self.expr1.reduce(), self.expr2.reduce())

    def __str__(self):
        return '{}{}{}'.format(str(self.expr1), str(self.op), str(self.expr2))
