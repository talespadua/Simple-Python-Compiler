from lexer.lexer import Lexer


class Node():

    labels = 0

    def __init__(self):
        self.lexline = Lexer.line
        
    def error(self, error_str=''):
        raise Exception(
            "Error near line {}: {}".format(self.lexline, error_str)
        )

    @classmethod
    def new_label(cls):
        cls.labels += 1
        return cls.labels

    @staticmethod
    def emit_label(i):
        print('L{}:'.format(str(i)))

    @staticmethod
    def emit(s):
        print('\t{}'.format(s))
