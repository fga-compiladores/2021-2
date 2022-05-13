import pytest
from lark import Lark
import re

GRAMMAR = re.compile(
    r"""
\*\*(G\d)\*\*\s*
```\s*
(.*?)
```
""",
    flags=re.MULTILINE | re.VERBOSE | re.DOTALL,
)


class TestAnswer:
    @pytest.fixture(scope="module")
    def data(self, floader):
        return floader("bnf.answer.md")

    @pytest.fixture(scope="module")
    def grammars(self, data):
        return {m.group(1): m.group(2).strip() for m in GRAMMAR.finditer(data)}

    def test_não_usa_operadores_extendidos(self, grammars):
        for k, src in grammars.items():
            assert "?" not in src, f"{k} possui um operador ?"
            assert "*" not in src, f"{k} possui um operador *"
            assert "+" not in src, f"{k} possui um operador +"


class TestSubmission(TestAnswer):
    @pytest.fixture(scope="module")
    def data(self, floader):
        return floader("bnf.md")
