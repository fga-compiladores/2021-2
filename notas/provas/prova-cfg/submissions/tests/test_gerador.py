from lark import Lark, LarkError
import pytest
import random
import re

NUMBER = re.compile(r"\d+")

grammar = Lark(
    """
start    : fizz

fizz     : "fizz"
         | "fizz(" fizz [ SEP buzz ] ")" 

buzz     : "buzz"
         | "buzz(" (NUMBER SEP)+ buzz ")"

SEP      : ", "
NUMBER   : /0|100|[1-9][0-9]?/
""",
    parser="lalr",
)


class TestAnswer:
    @pytest.fixture(scope="module")
    def rand(self, loader):
        return loader("gerador.answer").random_example

    def test_exemplos_obedecem_à_gramática(self, rand):
        random.seed(0)
        failed = []
        for _ in range(1000):
            ex = rand()
            try:
                assert grammar.parse(ex)
            except LarkError as exc:
                failed.append((ex, str(exc)))

        if failed:
            failed.sort(key=lambda t: len(t[0]))

            ex, error = failed[0]
            print(f"Exemplo incompatível com a gramática: {ex}")
            print(error)
        assert not failed

    def test_consegue_gerar_casos_simples(self, rand):
        non_generated = {
            "fizz",
            "fizz(fizz)",
            "fizz(fizz(fizz))",
            "fizz(fizz, buzz)",
            "fizz(fizz, buzz(N, buzz))",
            "fizz(fizz, buzz(N, N, buzz))",
        }
        for _ in range(1_000_000):
            ex = rand()
            ex = NUMBER.sub("N", ex)
            non_generated.discard(ex)
            if not non_generated:
                break

        assert not non_generated, "não conseguiu gerar alguns exemplos simples."

    def test_consegue_gerar_milhares_de_casos_diferentes(self, rand):
        exs = set()
        num_tries = 0

        while len(exs) < 10_000:
            exs.add(rand())
            num_tries += 1
            if num_tries > 1_000_000:
                break
        assert num_tries < 1_000_000


class TestSubmission(TestAnswer):
    @pytest.fixture(scope="module")
    def rand(self, loader):
        return loader("gerador").random_example
