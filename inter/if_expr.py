from .stmt import Stmt
from symbols.type import Type


class If(Stmt):

    def __init__(self, x, s):
        super().__init__()
        self.expr = x
        self.stmt = s
        if self.expr.type_ != Type.bool_:
            self.expr.error("boolean required in if")

    def gen(self, b, a):
        label = Stmt.new_label()
        self.expr.jumping(0, a)
        self.emit_label(label)
        self.stmt.gen(label, a)
