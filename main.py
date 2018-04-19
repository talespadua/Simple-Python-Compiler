from lexer.lexer import Lexer
from parser.parser import Parser
import sys


if __name__ == '__main__':
    file = sys.argv[1]
    lex = Lexer()
    parser = Parser(lex)
    parser.program()
    print('\n')
