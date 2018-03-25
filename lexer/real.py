from .token import Token
from .tag import Tag


class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value
