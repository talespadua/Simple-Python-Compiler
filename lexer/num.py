from .token import Token
from .tag import Tag


class Num(Token):
    def __init__(self, value):
        super().__init__(Tag.NUM)
        self.value = value

    def __str__(self):
        return str(self.value)