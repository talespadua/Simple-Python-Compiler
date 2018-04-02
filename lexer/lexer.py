import sys
from .token import Token
from .tag import Tag
from .word import Word
from .num import Num
from symbols.type import Type


class Lexer:
    line = 1

    def __init__(self):
        self.peek = ''
        self.words = {
            'true': Word.true,
            'false': Word.false,
            'if': Word(Tag.IF, 'if'),
            'else': Word(Tag.ELSE, 'else'),
            'while': Word(Tag.WHILE, 'while'),
            'do': Word(Tag.DO, 'do'),
            'break': Word(Tag.DO, 'break'),
            'int': Type.int_,
            'char': Type.char_,
            'float': Type.float_,
            'bool': Type.bool_,
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
                Lexer.line += 1
            else:
                break

        if self.peek == '&':
            if self.readch('&'):
                return Word.and_
            else:
                return Token('&')

        if self.peek == '|':
            if self.readch('|'):
                return Word.or_
            else:
                return Token('|')

        if self.peek == '=':
            if self.readch('='):
                return Word.eq
            else:
                return Token('=')

        if self.peek == '!':
            if self.readch('='):
                return Word.ne
            else:
                return Token('!')

        if self.peek == '<':
            if self.readch('='):
                return Word.le
            else:
                return Token('<')

        if self.peek == '>':
            if self.readch('='):
                return Word.ge
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
