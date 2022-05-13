import pytest


class TestAnswer:
    @pytest.fixture(scope="module")
    def parse(self, loader):
        return loader("arvores.answer").parse

    def test_exemplos_simples(self, parse):
        print(repr(parse("x;")))
        assert parse("x;") == "x"
        assert parse("print(x, y);") == ["print", "x", "y"]
        assert parse("x = y;") == ["def", "x", "y"]
        assert parse("if a { b; } else { c; }") == ["if", "a", "b", "c"]

    def test_exemplo_longo(self, parse):
        assert parse(
            """
            x = f(y);

            if f(z) {
                a(b(c), d);
            }
            else {
                f(a);
                f(b, c);
                d();
            }
            """
        ) == [
            "block",
            ["def", "x", ["f", "y"]],
            [
                "if",
                ["f", "z"],
                ["a", ["b", "c"], "d"],
                ["block", ["f", "a"], ["f", "b", "c"], ["d"]],
            ],
        ]


class TestSubmission(TestAnswer):
    @pytest.fixture(scope="module")
    def parse(self, loader):
        return loader("arvores").parse
