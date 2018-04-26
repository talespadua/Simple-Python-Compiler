from .node import Node


class Expr(Node):
    def __init__(self, token, type_):
        super().__init__()
        self.op = token
        self.type_ = type_

    def gen(self):
        return self

    def reduce(self):
        return self

    def jumping(self, t, f):
        self.emitjumps(str(self), t, f)

    def emitjumps(self, test, t, f):
        if t != 0 and f != 0:
            self.emit('if {} goto L{}'.format(test, str(t)))
            self.emit('goto L{}'.format(str(f)))
        elif t != 0:
            self.emit('if {} goto L{}'.format(test, str(t)))
        elif f != 0:
            self.emit('iffalse {} goto L{}'.format(test, str(f)))
        else:
            pass

    def __str__(self):
        return str(self.op)
