from symbols.type import Type
from .stmt import Stmt


class Do(Stmt):

    def __init__(self):
        # super().__init__()
        self.expr = None
        self.stmt = None

    def init(self, s, x):
        self.expr = x
        self.stmt = s
        if self.expr.type_p is not Type._bool():
            self.expr.error("Boolean requiered in do")

    def gen(self, b, a):
        self.after = a
        label = self.new_label()
        self.stmt.gen(b, label)
        self.emit_label(label)
        self.expr.jumping(b, 0)
