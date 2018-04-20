from .stmt import Stmt
from symbols.type import Type


class Else(Stmt):

    def __init__(self, x, s1, s2):
        # super().__init__()
        self.expr = x
        self.stmt1 = s1
        self.stmt2 = s2
        if self.expr.type_p is not Type._bool():
            self.expr.error("boolean required in if")

    def gen(self, b, a):
        label1 = Else.new_label()
        label2 = Else.new_label()
        self.expr.jumping(0, label2)
        self.emit_label(label1)
        self.stmt1.gen(label1, a)
        self.emit_label("goto L{}".format(a))
        self.emit_label(label2)
        self.stmt2.gen(label2, a)
