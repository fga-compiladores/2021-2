import lark
from lark.visitors import Transformer  # pip3 install lark-parser
from lark import Lexer

# EBNF
grammar = r"""
start  : value+

?value : list
       | quote
       | "#t" -> true
       | "#f" -> true
       | NUMBER 
       | STRING 
       | SYMBOL
       | OP

list   : "(" value* ")"

quote  : "`" value

%import common.ESCAPED_STRING -> STRING
%import common.SIGNED_NUMBER  -> NUMBER
%ignore /\s+/
%ignore /;[^\n]*/

SYMBOL : ("a" .. "z")+
OP     : ("+" | "-" | "*" | "/" | "=" | "!" | ">" | "<"| "?" | "@" )+ 
"""


class LISPTransformer(lark.Transformer):
    def NUMBER(self, st):
        return int(st)

    def STRING(self, st):
        return st[1:-1]

    def SYMBOL(self, st):
        return str(st)

    def OP(self, st):
        return self.SYMBOL(st)

    def list(self, children):
        return children


parser = lark.Lark(grammar)


def loads(text: str) -> object:
    """
    Carrega um documento JSON e retorna o valor Python correspondente.
    """
    tree = parser.parse(text)
    transformer = LISPTransformer()
    tree = transformer.transform(tree)
    if hasattr(tree, "pretty"):
        return tree.pretty()
    return tree


# Exemplos
print(loads("true"))
print(loads("false"))
print(loads("null"))
print(loads("42"))
print(loads('"Hello World"'))
print(loads("(true false null (1 2 3 ()))"))
print(
    loads(
        """
(define fat (n) 
    (if (= n 0) 
        1 
        (* n (fat (- n 1)))))
"""
    )
)
