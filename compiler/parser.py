import sys
from .exceptions import SyntaxException


class Parser:
    def __init__(self, expression):
        self.expression = expression

    def expr(self):
        self.term()
        while True:
            if self.expression.lookahead == '+':
                self.match('+')
                self.term()
                print('+')
            elif self.expression.lookahead == '-':
                self.match('-')
                self.term()
                print('-')
            else:
                return

    def term(self):
        if self.expression.lookahead.isdigit():
            print(self.expression.lookahead)
            self.match(self.expression.lookahead)
        else:
            raise SyntaxException

    def match(self, t):
        if self.expression.lookahead == t:
            self.expression.advance()
        else:
            print("syntax error")
