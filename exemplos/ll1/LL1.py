from multiprocessing.sharedctypes import Value
from typing import Dict, Iterable, List, Sequence, Mapping, Set
from collections import deque
from pprint import pprint

ε = None


def check_ll1(
    transition: Mapping[str, Mapping[str, Sequence[str]]],
    tokens: Iterable[str],
    start: str = "start",
    debug: bool = False,
) -> bool:
    """
    Verifica se uma lista de tokens é compatível com uma tabela de
    transição pelo método LL(1).
    """

    def is_terminal(symb: str):
        return symb not in transition

    tokens = deque([*tokens, "EOF"])
    actions = deque([start, "EOF"])

    while actions:
        if debug:
            print("# cmd:", " ".join(actions))
            print("# tks:", " ".join(tokens))
            print()

        symb = actions.popleft()
        if is_terminal(symb):
            tk = tokens.popleft()
            if tk != symb:
                return False
        else:
            dic = transition[symb]
            try:
                expansion = dic[tokens[0]]
            except KeyError:
                return False
            for e in reversed(expansion):
                actions.appendleft(e)

    return len(tokens) == 0


# ===========================================================================
# Exemplos
# ===========================================================================

# LISTAS
"""
0. start -> lst EOF
1. lst   -> [ elems ]    # FIRST([ elems ]) = { [ }
2. elems -> value tail   # FIRST(value tail) = { STR, NUM, [ }
3. tail  -> , elems      # FIRST(, elems) = { , }
4. tail  -> ε            # FIRST(ε) = { ε }
5. value -> STR          # FIRST(STR) = { STR }
6. value -> NUM          # FIRST(NUM) = { NUM }
7. value -> lst          # FIRST(lst) = { [ }

FIRST(lst) = { [ }
FIRST(elems) = { STR, NUM, [ }
FIRST(tail) = { ε, "," }
FIRST(value) = { STR, NUM, [ }

FOLLOW(lst) = { EOF, ], "," }
FOLLOW(elems) = { ] }
FOLLOW(tail) = { ] }
FOLLOW(value) = { ], "," }

+------+-----+-----+-----+-----+-----+-----+
|      |  [  |  ]  |  ,  | NUM | STR | EOF |
+======+=====+=====+=====+=====+=====+=====+
|lst   |  1  |     |     |     |     |     |
+------+-----+-----+-----+-----+-----+-----+
|elems |  2  |     |     |  2  |  2  |     |
+------+-----+-----+-----+-----+-----+-----+
|tail  |     |  4  |  3  |     |     |     |
+------+-----+-----+-----+-----+-----+-----+
|value |  7  |     |     |  6  |  5  |     |
+------+-----+-----+-----+-----+-----+-----+
"""

transition_list = {
    "start": {
        "[": ["lst"],
    },
    "lst": {
        "[": ["[", "elems", "]"],
    },
    "elems": {
        "[": ["value", "tail"],
        "NUM": ["value", "tail"],
        "STR": ["value", "tail"],
    },
    "tail": {
        "]": [],
        ",": [",", "elems"],
    },
    "value": {
        "[": ["lst"],
        "NUM": ["NUM"],
        "STR": ["STR"],
    },
}

grammar_list = {
    "lst": [
        ["[", "elems", "]"],
    ],
    "elems": [
        ["value", "tail"],
    ],
    "tail": [
        [",", "elems"],
        [],
    ],
    "value": [
        ["STR"],
        ["NUM"],
        ["lst"],
    ],
}


# LISTAS
"""
1. start -> expr             # FIRST(expr) = { NUM, OP }
2. expr  -> NUM              # FIRST(NUM) = { NUM } 
3. expr  -> OP expr expr     # FIRST(OP expr expr) = { OP }

FIRST(start) = { NUM, OP }
FIRST(expr) = { NUM, OP }

+-------+-----+-----+-----+
|       | NUM | OP  | EOF |
+=======+=====+=====+=====+
| start |  1  |  1  |     |
+-------+-----+-----+-----+
| expr  |  2  |  3  |     |
+-------+-----+-----+-----+
"""

grammar_prefix = {
    "start": [
        ["expr"],
    ],
    "expr": [
        ["NUM"],
        ["OP", "expr", "expr"],
    ],
}

transition_prefix = {
    "start": {
        "NUM": ["expr"],
        "OP": ["expr"],
    },
    "expr": {
        "NUM": ["NUM"],
        "OP": ["OP", "expr", "expr"],
    },
}


class LL1:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first = init_first(grammar)
        self.follow = init_follow(grammar, self.first)
        self.table = init_table(grammar, self.first, self.follow)


def init_first(grammar: Dict[str, List[List[str]]]) -> Dict[str, Set[str]]:
    def is_terminal(symb):
        return symb not in grammar

    # Inicializa cada não-terminal com um conjunto vazio
    first = {k: set() for k in grammar.keys()}

    # Executa até não haver mais mudanças nos conjuntos FIRST de cada
    # símbolo
    n_symbs = -1
    while n_symbs != (n_symbs_curr := sum(map(len, first.values()))):
        n_symbs = n_symbs_curr

        # Percorre cada regra da gramática
        for name, rule_list in grammar.items():
            for rule in rule_list:
                for symb in rule:
                    # Acrescenta simbolo ao FIRST(name), caso
                    # seja terminal. Não atualiza mais first[name]
                    if is_terminal(symb):
                        first[name].add(symb)
                        break
                    # Acrescenta todos elementos de FIRST(symb), caso
                    # seja não-terminal
                    else:
                        new = first[symb]
                        # Se FIRST(symb) contem ε, acrescentamos
                        # os símbolos (menos ε) e continuamos
                        # com o próximo elemento
                        if ε in new:
                            first[name].update(new - {ε})

                        # Interrompe se FIRST(symb) não contém ε
                        else:
                            first[name].update(new)
                            break

                # Acresenta um ε se todos os símbolos da regra
                # também contiverem um epsilon (não executou
                # nenhum break no código acima)
                else:
                    first[name].add(ε)
    return first


def init_follow(
    grammar: Dict[str, List[List[str]]],
    first: Dict[str, Set[str]],
    start: str,
) -> Dict[str, Set[str]]:
    def is_terminal(symb):
        return symb not in grammar

    # Inicializa cada não-terminal com um conjunto vazio
    # e acrescenta o EOF ao símbolo inicial
    follow = {k: set() for k in grammar.keys()}
    follow[start].add("EOF")

    # Executa até não haver mais mudanças nos conjuntos FIRST de cada
    # símbolo
    n_symbs = -1
    while n_symbs != (n_symbs_curr := sum(map(len, follow.values()))):
        n_symbs = n_symbs_curr

        # Percorre cada regra da gramática
        for name, rule_list in grammar.items():
            for rule in rule_list:
                # name -> rule
                for i, symb in enumerate(rule):
                    # name -> ... symb
                    #             ^^^^

                    # Atualizamos of FOLLOW(symb) para não-terminais
                    if is_terminal(symb):
                        continue

                    # Calculamos o conjunto first da expressão que
                    # segue o símbolo atual
                    tail = rule[i + 1 :]
                    tail_first = set(FIRST(tail, first))

                    # Se ε estiver presente, incluímos também o
                    # FOLLOW(name)
                    if ε in tail_first:
                        tail_first.discard(ε)
                        follow[symb].update(follow[name])

                    # Em todos os casos, incluímos o FIRST(tail)
                    # no conjunto follow
                    follow[symb].update(tail_first)

    return follow


def init_table(grammar, first, follow):
    table = {k: {} for k in grammar.keys()}

    for name, rule_list in grammar.items():
        for rule in rule_list:
            if len(rule) == 0:
                for terminal in follow[name]:
                    if terminal in table[name]:
                        raise ValueError("not LL1")
                    table[name][terminal] = rule
            else:
                for terminal in set(FIRST(rule, first)):
                    if terminal in table[name]:
                        raise ValueError("not LL1")
                    table[name][terminal] = rule

    return table


def FIRST(seq, first):
    is_terminal = lambda symb: symb not in first

    for symb in seq:
        if is_terminal(symb):
            yield symb
            break
        else:
            symbs = first[symb]
            if ε in symbs:
                yield from symbs - {ε}
            else:
                yield from symbs
                break
    else:
        yield ε


first_set = init_first(grammar_list)
follow_set = init_follow(grammar_list, first_set, start="lst")
pprint(init_table(grammar_list, first_set, follow_set))


# Exemplo: LISTA
# ex = "[ [ NUM , STR ] , NUM ]".split()
# print("Accept?", check_ll1(transition_list, ex, debug=True))


# Exemplo: OPS
# + 42 * + 10 12 1
# 42 + ((10 + 12) * 1)
# ex = "OP NUM OP OP NUM NUM NUM".split()
# print("Accept?", check_ll1(transition_prefix, ex, debug=True))
