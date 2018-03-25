import sys
from .exceptions import UnknownKeyword
from .token import Token
from .tag import Tag
from .word import Word
from .num import Num
from .real import Real
from symbols.type import Type
from symbols.array import Array


class Lexer:
    def __init__(self):
        self.line = 1
        self.peek = ''
        self.words = {
            'true': Word._true(),
            'false': Word._false(),
            'if': Word(Tag.IF, 'if'),
            'else': Word(Tag.ELSE, 'else'),
            'while': Word(Tag.WHILE, 'while'),
            'do': Word(Tag.DO, 'do'),
            'break': Word(Tag.DO, 'break'),
            'int': Type._int(),
            'char': Type._char(),
            'float': Type._float(),
            'bool': Type._bool(),
        }

    def readch(self, c=None):
        if c is None:
            self.peek = sys.stdin.read(1)
            return
        self.readch()
        if self.peek != c:
            return False
        self.peek = ''
        return True

    def scan(self):
        while True:
            self.readch()
            if self.peek == '' or self.peek == '\t':
                continue
            elif self.peek == '\n':
                self.line += 1
            else:
                break

        if self.peek == '&':
            if self.readch('&'):
                return Word._and()
            else:
                return Token('&')

        if self.peek == '|':
            if self.readch('|'):
                return Word._or()
            else:
                return Token('|')

        if self.peek == '=':
            if self.readch('='):
                return Word._eq()
            else:
                return Token('=')

        if self.peek == '!':
            if self.readch('='):
                return Word._ne()
            else:
                return Token('!')

        if self.peek == '<':
            if self.readch('='):
                return Word._le()
            else:
                return Token('<')

        if self.peek == '>':
            if self.readch('='):
                return Word._ge()
            else:
                return Token('>')

        if self.peek.isdigit():
            v = 0
            while True:
                v = 10*v + int(self.peek)
                self.peek = sys.stdin.read(1)
                if not self.peek.isdigit():
                    break
            return Num(v)

        if self.peek.isalpha():
            s = ''
            while True:
                s += self.peek
                self.peek = sys.stdin.read(1)
                if not self.peek.isalpha():
                    break
            w = self.words[s]
            if w:
                return w
            w = Word(Tag.ID, s)
            self.words[s] = w
            return w
        t = Token(self.peek)
        self.peek = ''
        return t
