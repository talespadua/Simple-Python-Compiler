from .token import Token
from .tag import Tag


class Word(Token):

    def __init__(self, lexeme, tag):
        super().__init__(tag)
        self.lexeme = lexeme

    def __str__(self):
        return self.lexeme

    @classmethod
    def _and(cls):
        return cls('&&', Tag.AND)

    @classmethod
    def _or(cls):
        return cls("||", Tag.OR)

    @classmethod
    def _eq(cls):
        return cls("==", Tag.EQ)

    @classmethod
    def _ne(cls):
        return cls("!=", Tag.NE)

    @classmethod
    def _le(cls):
        return cls("<=", Tag.LE)

    @classmethod
    def _ge(cls):
        return cls(">=", Tag.GE)

    @classmethod
    def _minus(cls):
        return cls("minus", Tag.MINUS)

    @classmethod
    def _true(cls):
        return cls("true", Tag.TRUE)

    @classmethod
    def _false(cls):
        return cls("false", Tag.FALSE)

    @classmethod
    def temp(cls):
        return cls("t", Tag.TEMP)