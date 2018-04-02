from .stmt import Stmt


class Break(Stmt):

    def __init__(self):
        super().__init__()
        if Stmt.enclosing is None:
            self.error("unenclosed break")
        self.stmt = Stmt.enclosing

    def gen(self, b, a):
        self.emit("goto L{}".format(self.stmt.after))
