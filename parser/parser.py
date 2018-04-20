from .exceptions import SyntaxException
from lexer.tag import Tag
from lexer.word import Word
from lexer.token import Token
from symbols.env import Env
from symbols.array import Array
from symbols.type import Type
from inter.id import Id
from inter.stmt import Stmt
from inter.seq import Seq
from inter.if_expr import If
from inter.else_expr import Else
from inter.while_expr import While
from inter.do import Do
from inter.set import Set
from inter.set_elem import SetElem
from inter.or_expr import Or
from inter.and_expr import And
from inter.rel import Rel
from inter.arith import Arith
from inter.unary import Unary
from inter.not_expr import Not
from inter.constant import Constant
from inter.access import Access


class Parser:

    def __init__(self, l):
        self.lex = l
        self.look = None
        self.top = None
        self.s = None
        self.used = 0
        self.move()

    def move(self):
        self.look = self.lex.scan()

    def error(self, s):
        raise SyntaxException("near line {}: {}".format(self.lex.line, s))

    def match(self, t):
        if self.look.tag == t:
            self.move()
        else:
            self.error("syntax error")

    def program(self):
        self.s = self.block()
        begin = self.s.new_label()
        after = self.s.new_label()
        self.s.emit_label(begin)
        self.s.gen(begin, after)
        self.s.emit_label(after)

    def block(self):
        self.match('{')
        saved_env = self.top
        self.top = Env(self.top)
        self.decls()
        s = self.stmts()
        self.match('}')
        self.top = saved_env
        return s

    def decls(self):
        while self.look.tag == Tag.BASIC:
            p = self.get_type()
            tok = self.look
            self.match(Tag.ID)
            self.match(';')
            id_ = Id(tok, p, self.used)
            self.top.put(tok, id_)
            self.used = self.used + p.width

    def get_type(self):
        p = self.look
        self.match(Tag.BASIC)
        if self.look.tag != '[':
            return p
        else:
            return self.dims(p)

    def dims(self, p):
        self.match('[')
        tok = self.look
        self.match(Tag.NUM)
        self.match(']')
        if self.look.tag == '[':
            p = self.dims(p)
        return Array(tok.value, p)

    def stmts(self):
        if self.look.tag == '{':
            return Stmt.null
        else:
            return Seq(self.stmt(), self.stmts)

    def stmt(self):
        if self.look.tag == ';':
            self.move()
            return Stmt.null
        elif self.look.tag == Tag.IF:
            self.match(Tag.IF)
            self.match('(')
            x = self.bool_()
            self.match(')')
            s1 = self.stmt()
            if self.look.tag is not Tag.ELSE:
                return If(x, s1)
            self.match(Tag.ELSE)
            s2 = self.stmt()
            return Else(x, s1, s2)
        elif self.look.tag == Tag.WHILE:
            while_node = While()
            saved_stmt = Stmt.enclosing
            Stmt.enclosing = while_node
            self.match(Tag.WHILE)
            self.match('(')
            x = self.bool_()
            self.match(')')
            s1 = self.stmt()
            while_node.init(x, s1)
            Stmt.enclosing = saved_stmt
        elif self.look.tag == Tag.DO:
            donode = Do()
            saved_stmt = Stmt.enclosing
            Stmt.enclosing = donode
            self.match(Tag.DO)
            s1 = self.stmt()
            self.match(Tag.WHILE)
            self.match('(')
            x = self.bool_()
            self.match(')')
            self.match(';')
            donode.init(s1, x)
            Stmt.enclosing = saved_stmt
            return donode
        elif self.look.tag == Tag.BREAK:
            self.match(Tag.BREAK)
            self.match(';')
        elif self.look.tag == '{':
            return self.block()
        else:
            return self.assign()

    def assign(self):
        t = self.look
        self.match(Tag.ID)
        id_ = self.top.get(t)
        if id_ is None:
            self.error("{} undeclared".format(str(t)))
        if self.look.tag == '=':
            self.move()
            stmt = Set(id_, self.bool_())
        else:
            x = self.offset(id_)
            self.match('=')
            stmt = SetElem(x, self.bool_())
        self.match(';')
        return stmt

    def bool_(self):
        x = self.join()
        while self.look.tag == Tag.OR:
            tok = self.look
            self.move()
            x = Or(tok, x, self.join())
        return x

    def join(self):
        x = self.equality()
        while self.look.tag == Tag.AND:
            tok = self.look
            self.move()
            x = And(tok, x, self.equality())
        return x

    def equality(self):
        x = self.rel()
        while self.look .tag == Tag.EQ or self.look.tag == Tag.NE:
            tok = self.look
            self.move()
            x = Rel(tok, x, self.rel())
        return x

    def rel(self):
        x = self.expr()
        if (self.look.tag == '<' or self.look.tag == '>' or
                self.look.tag == Tag.LE or self.look.tag == Tag.GE):
            tok = self.look
            self.move()
            return Rel(tok, x, self.expr())
        else:
            return x

    def expr(self):
        x = self.term()
        while self.look.tag == '+' or self.look.tag == '-':
            tok = self.look
            self.move()
            x = Arith(tok, x, self.term())
        return x

    def term(self):
        x = self.unary()
        while self.look.tag == '*' or self.look.tag == '/':
            tok = self.look
            self.move()
            x = Arith(tok, x, self.unary())
        return x

    def unary(self):
        if self.look.tag == '-':
            self.move()
            return Unary(Word.minus, self.unary())
        elif self.look.tag == '!=':
            tok = self.look
            self.move()
            return Not(tok, self.unary())
        return self.factor()

    def factor(self):
        x = None
        if self.look.tag == '(':
            self.move()
            x = self.bool_()
            self.match(')')
            return x
        elif self.look.tag == Tag.NUM:
            x = Constant(token=self.look, type_=Type.int_)
            self.move()
            return x
        elif self.look.tag == Tag.REAL:
            x = Constant(token=self.look, type_=Type.float_)
            self.move()
            return x
        elif self.look.tag == Tag.TRUE:
            x = Constant.true
            self.move()
            return x
        elif self.look.tag == Tag.FALSE:
            x = Constant.false
            self.move()
            return x
        elif self.look.tag == Tag.ID:
            id_ = self.top.get(self.look)
            if id_ is None:
                self.error("{} undeclared".format(str(self.look)))
            self.move()
            if self.look.tag != '[':
                return id_
            return self.offset(id_)
        else:
            self.error("syntax error")
            return x

    def offset(self, a):
        type_ = a.type_
        self.match('[')
        i = self.bool_()
        self.match(']')
        type_ = Array(1, type_.of)
        w = Constant(i=type_.width)
        t1 = Arith(Token('*'), i, w)
        loc = t1
        while self.look.tag == '[':
            self.match('[')
            i = self.bool_()
            self.match(']')
            type_ = Array(1, type_.of)
            w = Constant(i=type_.width)
            t1 = Arith(Token('*'), i, w)
            t2 = Arith(Token('+'), loc, t1)
            loc = t2
        return Access(a, loc, type_)




