from .stmt import Stmt


class Seq(Stmt):

    def __init__(self, s1, s2):
        super().__init__()
        self.stmt1 = s1
        self.stmt2 = s2

    def gen(self, b, a):
        if self.stmt1 is Stmt.null:
            self.stmt2.gen(b, a)
        elif self.stmt2 is Stmt.null:
            self.stmt1.gen(b, a)
        else:
            label = Stmt.new_label()
            self.stmt1.gen(b, label)
            self.emit_label(label)
            self.stmt2.gen(label, a)
