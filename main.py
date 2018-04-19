from parser.expression import Expression
from parser.parser import Parser

if __name__ == '__main__':
    input = 'int a = 1+2;'
    expression = Expression(input)
    parser = Parser(expression)
    parser.expr()