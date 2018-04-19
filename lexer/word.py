from .token import Token
from .tag import Tag


class MetaWord(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        cls.and_ = cls('&&', Tag.AND)
        cls.or_ = cls("||", Tag.OR)
        cls.eq = cls("==", Tag.EQ)
        cls.ne = cls("!=", Tag.NE)
        cls.le = cls("<=", Tag.LE)
        cls.ge = cls(">=", Tag.GE)
        cls.minus = cls("minus", Tag.MINUS)
        cls.true = cls("true", Tag.TRUE)
        cls.false = cls("false", Tag.FALSE)
        cls.temp = cls("t", Tag.TEMP)


class Word(Token, metaclass=MetaWord):

    def __init__(self, lexeme, tag_id):
        super().__init__(tag_id)
        self.lexeme = lexeme

    def __str__(self):
        return self.lexeme

