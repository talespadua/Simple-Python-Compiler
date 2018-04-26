from .logical import Logical


class And(Logical):
    def __init__(self, token, x1, x2):
        super().__init__(token, x1, x2)

    def jumping(self, t, f):
        if f != 0:
            label = f
        else:
            label = self.new_label()
        self.expr1.jumping(0, label)
        self.expr2.jumping(t, f)
        if f == 0:
            self.emit_label(label)
