import sys
from .exceptions import UnknownKeyword
from .token import Token
from .tag import Tag
from .word import Word
from .num import Num
from .real import Real


class Lexer:
    def __init__(self):
        self.line = 1
        self.peek = ''
        self.words = {
            'true': Word(Tag.TRUE, 'true'),
            'false': Word(Tag.FALSE, 'false'),
            'if': Word(Tag.IF, 'if'),
            'else': Word(Tag.ELSE, 'else'),
            'while': Word(Tag.WHILE, 'while'),
            'do': Word(Tag.DO, 'do'),
            'break': Word(Tag.DO, 'break'),
            'int': Word(Tag.DO, 'break'),
            'char': Word(Tag.DO, 'break'),
            'float': Word(Tag.DO, 'break'),
            'bool': Word(Tag.DO, 'break'),
        }

    def scan(self):
        while True:
            self.peek = sys.stdin.read()
            if self.peek == '' or self.peek == '\t':
                continue
            elif self.peek == '\n':
                self.line += 1
            else:
                break
        if self.peek.isdigit():
            v = 0
            while True:
                v = 10*v + int(self.peek)
                self.peek = sys.stdin.read()
                if not self.peek.isdigit():
                    break
            return Num(v)

        if self.peek.isalpha():
            s = ''
            while True:
                s += self.peek
                self.peek = sys.stdin.read()
                if not self.peek.isalpha():
                    break
            w = self.words[s]
            if w:
                return w
            w = Word(Tag.ID, s)
            self.words[s] = w
            return w
        t = Token(self.peek)
        self.peek = ' '
        return t
