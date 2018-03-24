import sys
# class Expression():
# 
#     def __init__(self, expression):
#         self.expression = expression
#         self.index = 0
# 
#     @property
#     def lookahead(self):
#         lookahead = self.expression[self.index]
#         self.index += 1
#         return lookahead


class Parser:
    def __init__(self):
        self.lookahead = sys.stdin.read()

    def expr(self):
        self.term()
        while True:
            if self.lookahead == '+':
                self.match('+')
                self.term()
                print('+')
            elif self.lookahead == '-':
                self.match('-')
                self.term()
                print('-')
            else:
                return

    def term(self):
        if self.lookahead.isalpha():
            print(self.lookahead)
            self.match(self.lookahead)

    def match(self, t):
        if self.lookahead == t:
            self.lookahead = sys.stdin.read()
        else:
            print("syntax error")


if __name__ == '__main__':
    parser = Parser()
    parser.expr()
