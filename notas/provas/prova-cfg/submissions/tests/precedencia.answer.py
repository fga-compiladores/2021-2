"""
A calculadora abaixo possui regras de precedência e associatividade incorretas. Modifique 
a gramática para consertar tais erros.

Associatividade:
    esquerda: + - * /
    direita: ^

Precedência (da menor para a maior): 
    + -
    * /
    ^
"""
from lark import Lark, Transformer, v_args


grammar = Lark(
    r"""
start  : expr

?expr  : expr "+" term  -> add 
       | expr "-" term  -> sub
       | term

?term  : term "*" pow   -> mul
       | term "/" pow   -> div
       | pow

?pow   : atom "^" pow   -> pow
       | atom

?atom  : NUMBER
       | "(" expr ")"

NUMBER : /\d+(\.\d+)?/
%ignore /\s+/
"""
)


@v_args(inline=True)
class Calc(Transformer):
    from operator import add, sub, mul, truediv as div, pow

    NUMBER = float

    def start(self, expr):
        return expr


def eval_calc(src):
    ast = grammar.parse(src)
    return Calc().transform(ast)


if __name__ == "__main__":
    ops = "+-*/^"

    for op1 in ops:
        for op2 in ops:
            src = f"1.0 {op1} 2.0 {op2} 3.0"
            calc = eval_calc(src)
            py = eval(src.replace("^", "**"))
            if abs(calc - py) > 1e-9:
                print(f"{src} => {calc} (esperava {py})")
