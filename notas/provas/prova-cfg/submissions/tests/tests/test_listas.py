from lark import Lark, LarkError
import pytest
import re

lark = re.compile(r"```lark\n(?P<src>[^`]*)\n```", flags=re.MULTILINE)


class TestAnswer:
    @pytest.fixture(scope="module")
    def src(self, floader):
        return floader("listas.answer.md")

    @pytest.fixture(scope="module")
    def defs(self, src):
        grammars = [m.group("src") + "\nE : /E/" for m in lark.finditer(src)]
        del grammars[0]
        return dict(zip(["py", "js", "lisp"], grammars))

    @pytest.fixture(scope="module")
    def grammars(self, defs):
        return {k: Lark(v, start="lst") for k, v in defs.items()}

    @pytest.fixture(scope="module")
    def py(self, grammars):
        return grammars["py"]

    @pytest.fixture(scope="module")
    def js(self, grammars):
        return grammars["js"]

    @pytest.fixture(scope="module")
    def lisp(self, grammars):
        return grammars["lisp"]

    def test_todas_as_gramáticas_são_válidas(self, defs):
        for lang, grammar in defs.items():
            try:
                Lark(grammar, start="lst")
            except Exception as ex:
                print(f"gramática *{lang}* inválida")
                raise

    def grammar_check(self, grammar, valid, invalid):
        for ex in valid:
            assert grammar.parse(ex), f"falhou em exemplo válido de código: {ex}"

        for ex in invalid:
            with pytest.raises(LarkError):
                grammar.parse(ex)

    def test_py(self, py):
        self.grammar_check(
            py,
            valid=["[]", "[E]", "[E, E]", "[E, E,]"],
            invalid=["[,]", "[E,,E]", "[E,,]"],
        )

    def test_js(self, js):
        self.grammar_check(
            js,
            valid=["[]", "[E]", "[E, E]", "[E, E,]", "[E,,E]", "[E,,]"],
            invalid=["[,]"],
        )

    def test_lisp(self, lisp):
        self.grammar_check(
            lisp,
            valid=["()", "(E)", "(E E)", "(E E E)"],
            invalid=["[E E]", "(E, E)"],
        )


class TestSubmission(TestAnswer):
    @pytest.fixture(scope="module")
    def src(self, floader):
        return floader("listas.md")
