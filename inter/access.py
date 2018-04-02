from lexer.tag import Tag
from lexer.word import Word
from .op import Op


class Access(Op):

    def __init__(self, a, i, p):
        super().__init__(Word("[]", Tag.INDEX), p)
        self.array = a
        self.index = i

    def gen(self):
        return self.__class__(self.array, self.index.reduce(), self.type_p)

    def jumping(self, t, f):
        self.emitjumps(self.reduce().__str__(), t, f)

    def __str__(self):
        return '{}[{}]'.format(str(self.array), str(self.index))