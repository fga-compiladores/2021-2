from typing import Iterable


PUNCTUATION = set(".,:!?()[]@;'\"")


class Token(str):
    def __new__(cls, data, type):
        return str.__new__(cls, data)

    def __init__(self, data, type):
        self.type = type


def lex(src: str) -> Iterable[Token]:
    """
    Realiza a análise léxica de um texto em Português.

    Retorna uma sequência de tokens.
    """
    parts = src.split()
    parts.reverse()
    while parts:
        part = parts.pop()
        yield from _lex_part(part)


def _lex_part(st: str) -> Iterable:
    if not st:
        return
    elif st[0] in PUNCTUATION:
        yield Token(st[0], "PUNCTUATION")
        yield from _lex_part(st[1:])
    elif st[0].isalpha():
        yield from _lex_chars(st, str.isalpha, "WORD")
    elif st[0].isdigit():
        yield from _lex_chars(st, str.isdigit, "NUMBER")
    else:
        raise ValueError(f"caractere inválido: {st[0]}")


def _lex_chars(st, f, kind):
    i = 0
    while i < len(st) and f(st[i]):
        i += 1
    yield Token(st[:i], kind)
    yield from _lex_part(st[i:])


exemplo = """
A primeira etapa lê a entrada de caracteres, um de cada vez, mudando o estado em que os caracteres se encontram. Quando o analisador encontra um caractere que ele não identifica como correto, ele o chama de "estado morto" então, ele volta à última análise que foi aceita e assim tem o tipo e comprimento do léxico válido.

Um léxico, entretanto, é uma única lista de caracteres conhecidas de ser um tipo correto. Para construir um símbolo, o analisador léxico necessita de um segundo estado.
"""

for tk in lex(exemplo):
    print(f"{tk.type}: {tk}")
