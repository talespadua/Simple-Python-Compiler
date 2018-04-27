from .logical import Logical


class Or(Logical):
    def __init__(self, token, x1, x2):
        super().__init__(token, x1, x2)

    def jumping(self, t, f):
        if t != 0:
            label = t
        else:
            label = self.new_label()
        self.expr1.jumping(label, 0)
        self.expr2.jumping(t, f)
        if t == 0:
            self.emit_label(label)
