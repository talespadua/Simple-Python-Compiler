from inter.node import Node


class Stmt(Node):

    def __init__(self):
        super().__init__()
        self.after = 0

    def gen(self, b, a):
        pass

Stmt.null = Stmt()
Stmt.enclosing = Stmt.null
