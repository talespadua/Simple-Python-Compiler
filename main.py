from compiler.expression import Expression
from compiler.parser import Parser
from compiler.exceptions import EndOfExpressionException

if __name__ == '__main__':
    # TODO: Get this from input file
    expression = Expression('1+2')
    parser = Parser(expression)
    try:
        parser.expr()
    except EndOfExpressionException:
        print("end of expression")
