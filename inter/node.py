from lexer.lexer import Lexer


class Node:

    labels = 0

    def __init__(self):
        self.lexline = Lexer.line
        
    def error(self, error_str=''):
        raise Exception(
            "Error near line {}: {}".format(Lexer.line, error_str)
        )

    def new_label(self):
        self.labels += 1
        return self.labels

    def emit_label(self, i):
        print('L{}:'.format(str(i)), end='')

    def emit(self, s):
        print('\t{}'.format(s))
