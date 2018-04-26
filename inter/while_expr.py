from symbols.type import Type
from .stmt import Stmt


class While(Stmt):

    def __init__(self):
        super().__init__()
        self.expr = None
        self.stmt = None

    def init(self, x, s):
        self.expr = x
        self.stmt = s
        if self.expr.type_ is not Type.bool_:
            self.expr.error("Boolean required in while")

    def gen(self, b, a):
        self.after = a
        self.expr.jumping(0, a)
        label = While.new_label()
        self.emit_label(label)
        self.stmt.gen(label, b)
        self.emit("goto L{}".format(b))
