from .expr import Expr
from lexer.num import Num
from symbols.type import Type
from lexer.word import Word


class Constant(Expr):
    def __init__(self, token=None, type_=None, i=None):
        if i:
            super().__init__(Num(i), Type.int_)
        else:
            super().__init__(token, type_)

Constant.true = Constant(token=Word.true, type_=Type.bool_)
Constant.false = Constant(token=Word.false, type_=Type.bool_)


def jumping(contant, t, f):
    if contant == Constant.true:
        contant.emit('goto L{}'.format(t))
    elif contant == Constant.false:
        contant.emit('goto L{}'.format(f))

Constant.jumping = jumping
