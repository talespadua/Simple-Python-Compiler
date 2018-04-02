from .token import Token
from .tag import Tag


# class MetaWord(type):
#
#     def __init__(cls, clsname, superclasses, attributedict):
#         cls.and_ = cls('&&', Tag.AND)
#         cls.or_ = cls("||", Tag.OR)
#         cls.eq = cls("==", Tag.EQ)
#         cls.ne = cls("!=", Tag.NE)
#         cls.le = cls("<=", Tag.LE)
#         cls.ge = cls(">=", Tag.GE)
#         cls.minus = cls("minus", Tag.MINUS)
#         cls.true = cls("true", Tag.TRUE)
#         cls.false = cls("false", Tag.FALSE)
#         cls.temp = cls("t", Tag.TEMP)


# class Word(Token, metaclass=MetaWord):
class Word(Token):

    def __init__(self, lexeme, tag):
        # super(self.__class__, self).__init__(tag)
        super().__init__(tag)
        self.lexeme = lexeme

    def __str__(self):
        return self.lexeme


Word.and_ = Word('&&', Tag.AND)
Word.or_ = Word("||", Tag.OR)
Word.eq = Word("==", Tag.EQ)
Word.ne = Word("!=", Tag.NE)
Word.le = Word("<=", Tag.LE)
Word.ge = Word(">=", Tag.GE)
Word.minus = Word("minus", Tag.MINUS)
Word.true = Word("true", Tag.TRUE)
Word.false = Word("false", Tag.FALSE)
Word.temp = Word("t", Tag.TEMP)
