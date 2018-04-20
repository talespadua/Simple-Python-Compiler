from .expr import Expr
from symbols.type import Type
from .temp import Temp


class Logical(Expr):
    def __init__(self, token, x1, x2):
        super().__init__(token, None)
        self.expr1 = x1
        self.expr2 = x2
        self.type_ = self.check(self.expr1.type_, self.expr2.type_)
        if self.type_ is None:
            self.error('Type Error')

    @staticmethod
    def check(p1, p2):
        if p1 == Type._bool() and p2 == Type._bool():
            return Type._bool()
        else:
            return None

    def gen(self):
        f = self.new_label()
        a = self.new_label()
        temp = Temp(self.type_)
        self.jumping(0, f)
        self.emit('{} = true'.format(str(temp)))
        self.emit('goto L{}'.format(str(a)))
        Logical.emit_label(f)
        self.emit('{} = false'.format(str(temp)))
        Logical.emit_label(str(a))
        return temp

    def __str__(self):
        return '{} {} {}'.format(str(self.expr1), str(self.op), str(self.expr2))
