from lexer.word import Word
from lexer.tag import Tag


class Type(Word):
    def __init__(self, word, tag_id, w):
        super().__init__(word, tag_id)
        self.width = w

    @classmethod
    def numeric(cls, p):
        if p is cls.char_ or p is cls.int_ or p is cls.float_:
            return True
        return False

    @classmethod
    def max(cls, p1, p2):
        if not cls.numeric(p1) or not cls.numeric(p2):
            return None
        elif p1 is cls.float_ or p2 is cls.float_:
            return cls.float_
        elif p1 is cls.int_ or p2 is cls.int_:
            return cls.int_
        return cls.char_


Type.int_ = Type('int', Tag.BASIC, 4)
Type.float_ = Type('float', Tag.BASIC, 8)
Type.char_ = Type('char', Tag.BASIC, 1)
Type.bool_ = Type('bool', Tag.BASIC, 1)
