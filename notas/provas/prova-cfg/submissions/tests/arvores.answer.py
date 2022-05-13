"""
Modifique a gramática abaixo e/ou a classe de transformer para que as árvores
sintáticas dos exemplos abaixo obedeçam à estrutura desejada.

Você pode criar novas regras, reescrever as regras apresentadas, incluir operadores 
como ?, _, etc. 
"""
from lark import Lark, Transformer, Tree, v_args


grammar = Lark(
    r"""

?start : block

?block : cmd+

?cmd   : expr ";"
       | NAME "=" expr ";"  -> assign
       | "if" expr "{" block "}" "else" "{" block "}" -> cond

?expr  : NAME               -> var 
       | NAME "(" args ")"  -> funcall

args   : [ expr ("," expr)* ]

NAME   : /(?!\d)\w+/

%ignore /\s+/
"""
)


@v_args(inline=True)
class IR(Transformer):
    NAME = str
    var = str

    def funcall(self, fn, args):
        return [fn, *args]

    def args(self, *args):
        return args

    def assign(self, lhs, rhs):
        return ["def", lhs, rhs]

    def cond(self, cond, then, other):
        return ["if", cond, then, other]

    def block(self, *args):
        return ["block", *args]


def parse(src: str) -> Tree:
    ast = grammar.parse(src)
    return IR().transform(ast)
