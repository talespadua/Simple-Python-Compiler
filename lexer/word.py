from .token import Token
from .tag import Tag


class Word(Token):
    def __init__(self, lexeme, tag_id):
        super().__init__(tag_id)
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