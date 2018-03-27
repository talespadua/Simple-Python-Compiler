from lexer.word import Word
from lexer.tag import Tag


class Type(Word):
    def __init__(self, word, tag_id, w):
        super().__init__(word, tag_id)
        self.width = w

    @classmethod
    def _int(cls):
        return cls('int', Tag.BASIC, 4)

    @classmethod
    def _float(cls):
        return cls('float', Tag.BASIC, 8)

    @classmethod
    def _char(cls):
        return cls('char', Tag.BASIC, 1)

    @classmethod
    def _bool(cls):
        return cls('bool', Tag.BASIC, 1)

    @classmethod
    def numeric(cls, p):
        if p is cls._char() or p is cls._int() or p is cls._float():
            return True
        return False

    @classmethod
    def max(cls, p1, p2):
        if not cls.numeric(p1) or not cls.numeric(p2):
            return None
        elif p1 is cls._float() or p2 is cls._float():
            return cls._float()
        elif p1 is cls._int() or p2 is cls._int():
            return cls._int()
        return cls._char()