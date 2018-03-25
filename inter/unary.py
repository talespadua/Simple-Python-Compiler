from .op import Op
from symbols.type import Type


class Unary(Op):
    def __init__(self, token, ex):
        super().__init__(token, None)
        self.expr_ = ex
        self.type_ = Type.max(Type._int(), ex.type)
        if self.type is None:
            self.error()

    def gen(self):
        return self.__class__(self.op, self.expr_.reduce())

    def __str__(self):
        return '{}+{}'.format(str(self.op), str(self.expr_))
