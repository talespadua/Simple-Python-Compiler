from inter.node import Node


class MetaStmt(type):

    def __init__(cls):
        cls.null = cls()
        cls.enclosing = cls.null

class Stmt(Node, metaclass=MetaStmt):

    def __init__(self):
        super(self.__class__, self).__init__()
        super().__init__()
        self.after = 0

    def gen(self, b, a):
        pass