from lark import Lark, Token, Transformer, v_args


@v_args(inline=True)
class CalcTransformer(Transformer):
    from operator import add, mul, sub, truediv as div, pow

    def INT(self, tk):
        return int(tk)

    def FLOAT(self, tk):
        return float(tk)

    def start(self, elem):
        return elem


GRAMMAR = r"""
start : expr

?expr : expr "+" term   -> add
      | expr "-" term   -> sub
      | term

?term : term "*" elem   -> mul
      | term "/" elem   -> div
      | elem

?elem : atom  "^" elem  -> pow
      | atom
    
?atom : INT
      | FLOAT
      | NAME
      | "(" expr ")"

INT   : ("0" .. "9")+
FLOAT : INT "." INT
NAME  : ("a" .. "z")+

%ignore " " | "\n" | "\t"
"""

lark = Lark(GRAMMAR, parser="lalr")


def eval(st: str):
    transformer = CalcTransformer({"x": 42})
    ast = lark.parse(st)
    return transformer.transform(ast)


for ex in [
    "40.1 + 2",
    "40 * 2",
    "42",
    "1 + 2 + 3",
    "10 - 1 - 2",
    "10 ^ 3 ^ 2",
    "5 + 2 * 3",
    "2 ^ 3 * 3 ^ 2",
]:
    print(ex + " =", eval(ex))
