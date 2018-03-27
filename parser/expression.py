from .exceptions import EndOfExpressionException

class Expression:

    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    @property
    def lookahead(self):
        try:
            return self.expression[self.index]
        except EndOfExpressionException:
            raise EndOfExpressionException

    def advance(self):
        self.index += 1
