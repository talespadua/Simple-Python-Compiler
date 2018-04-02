from .stmt import Stmt
from symbols.type import Type


class If(Stmt):

    def __init__(self, x, s):
        super().__init__()
        self.expr = x
        self.stmt = s
        if self.expr.type_p != Type._bool():
            self.expr.error("boolean required in if")

    def gen(self, b, a):
        label = If.new_label()
        self.expr.jumping(0, a)
        self.emit_label(label)
        self.stmt.gen(label, a)
