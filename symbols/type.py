from lexer.word import Word, MetaWord
from lexer.tag import Tag


class MetaType(MetaWord):
    def __init__(cls, name, bases, attrs, **kwargs):
        cls.int_ = cls('int', Tag.BASIC, 4)
        cls.float_ = cls('float', Tag.BASIC, 8)
        cls.char_ = cls('char', Tag.BASIC, 1)
        cls.bool_ = cls('bool', Tag.BASIC, 1)


class Type(Word, metaclass=MetaType):
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
