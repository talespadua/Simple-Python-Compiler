from .expr import Expr
from lexer.word import Word


class Temp(Expr):
    count = 0

    def __init__(self, type_p):
        super().__init__(Word.temp(), type_p)
        Temp.count += 1
        self.number = Temp.count

    def __str__(self):
        return 't{}'.format(self.number)
