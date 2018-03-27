from .expr import Expr
from lexer.num import Num
from symbols.type import Type
from lexer.word import Word


class Constant(Expr):
    def __init__(self, token, type_p, i=None):
        if i:
            super().__init__(Num(i), Type._int())
        else:
            super().__init__(token, type_p)

    @classmethod
    def _true(cls):
        return cls(Word._true(), Type._bool())

    @classmethod
    def _false(cls):
        return cls(Word._false(), Type._bool())

    def jumping(self, t, f):
        if self == self.__class__._true():
            self.emit('goto L{}'.format(t))
        elif self == self.__class__._false():
            self.emit('goto L{}'.format(f))
