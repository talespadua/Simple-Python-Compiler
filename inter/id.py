from .expr import Expr


class Id(Expr):
    def __init__(self, word_id, type_p, int_b):
        super().__init__(word_id, type_p)
        self.offset = int_b
