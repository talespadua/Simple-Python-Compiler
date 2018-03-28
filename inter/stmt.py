from inter.node import Node

class Stmt(Node):

    def __init__(self):
        super.__init__(self)
        self.null = self
        self.after = 0
        self.enclosing = Stmt.null

    def gen(self, b, a):
        return self