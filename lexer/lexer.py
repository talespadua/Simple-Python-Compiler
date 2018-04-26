import sys
from .token import Token
from .tag import Tag
from .word import Word
from .num import Num
from symbols.type import Type
from parser.exceptions import EndOfExpressionException


class Lexer:
    line = 1

    def read_char(self):
        peek = self.file.read(1)
        if len(peek) < 1:
            raise EndOfExpressionException()
        return peek

    def __init__(self, file):
        self.peek = None
        self.words = {
            'true': Word.true,
            'false': Word.false,
            'if': Word('if', Tag.IF),
            'else': Word('else', Tag.ELSE),
            'while': Word('while', Tag.WHILE),
            'do': Word('do', Tag.DO),
            'break': Word('break', Tag.BREAK),
            'int': Type.int_,
            'char': Type.char_,
            'float': Type.float_,
            'bool': Type.bool_,
        }
        self.file = file

    def readch(self, c=None):
        if c is None:
            try:
                self.peek = self.read_char()
            except EndOfExpressionException:
                print("EOF")
            return
        self.readch()
        if self.peek != c:
            return False
        self.peek = None
        return True

    def scan(self):
        while True:
            if self.peek is None or self.peek == ' ' or self.peek == '\t' or self.peek == '':
                self.readch()
            elif self.peek == '\n':
                Lexer.line += 1
                self.readch()
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
                try:
                    self.peek = self.read_char()
                except EndOfExpressionException:
                    print("EOF")
                    return
                if not self.peek.isdigit():
                    break
            return Num(v)

        if self.peek.isalpha():
            s = ''
            while True:
                s += self.peek
                try:
                    self.peek = self.read_char()
                except EndOfExpressionException:
                    print("EOF")
                    return
                if not self.peek.isalpha():
                    break
            w = self.words.get(s)
            if w:
                return w
            w = Word(s, Tag.ID)
            self.words[s] = w
            return w
        t = Token(self.peek)
        self.peek = ''
        return t
