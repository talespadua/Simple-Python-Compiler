import sys


class Token:
    def __init__(self, tag):
        self.tag = tag


class Num(Token):
    def __init__(self, value):
        super().__init__(Tag.NUM)
        self.value = value


class Word(Token):
    def __init__(self, tag, lexame):
        super().__init__(tag)
        self.lexeme = lexame


class Tag:
    NUM = 256
    ID = 257
    TRUE = 258
    FALSE = 259


class Lexer:
    def __init__(self):
        self.line = 1
        self.peek = ''
        self.words = {
            'true': Word(Tag.TRUE, 'true'),
            'false': Word(Tag.FALSE, 'false')
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
