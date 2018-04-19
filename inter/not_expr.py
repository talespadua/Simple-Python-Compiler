from .logical import Logical


class Not(Logical):
    def __init__(self, token, x2):
        super().__init__(token, x2, x2)

    def jumping(self, t, f):
        self.expr2.jumping(f, t)

    def __str__(self):
        return '{}{}'.format(str(self.op), str(self.expr2))