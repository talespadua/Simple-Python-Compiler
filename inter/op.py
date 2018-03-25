from .expr import Expr



class Op(Expr):
    def __init__(self, token, type_p):
        super().__init__(token, type_p)

    def reduce(self):
        x = self.gen()
        t = Temp()
        self.emit('{} = {}'.format(str(t), str(x)))
        return t