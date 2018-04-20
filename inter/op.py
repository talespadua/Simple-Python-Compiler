from .expr import Expr
from .temp import Temp


class Op(Expr):
    def __init__(self, token, type_):
        super().__init__(token, type_)

    def reduce(self):
        x = self.gen()
        t = Temp()
        self.emit('{} = {}'.format(str(t), str(x)))
        return t