from .type import Type
from lexer.tag import Tag


class Array(Type):
    def __init__(self, size, _type):
        super().__init__('[]', Tag.INDEX, size*_type.width)
        self.size = size
        self.of = _type

    def __str__(self):
        return '[{}] {}'.format(self.size, str(self.of))
