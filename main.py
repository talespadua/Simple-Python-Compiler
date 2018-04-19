from lexer.lexer import Lexer
from parser.parser import Parser
import sys
from os import path


if __name__ == '__main__':
    file_name = sys.argv[1]
    file_name = path.join(path.dirname(__file__), file_name)
    with open(file_name) as f:
        lex = Lexer(f)
        parser = Parser(lex)
        parser.program()
    print('\n')
