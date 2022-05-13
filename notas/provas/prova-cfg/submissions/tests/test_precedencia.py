import pytest


class TestAnswer:
    @pytest.fixture(scope="module")
    def calc(self, loader):
        return loader("precedencia.answer").eval_calc

    def test_exemplos_simples(self, calc):
        assert calc("40 + 2") == 42.0
        assert calc("21 * 2") == 42.0
        assert calc("50 - 8") == 42.0
        assert calc("84 / 2") == 42.0
        assert calc("2 ^ 3") == 8.0

    def test_cadeias(self, calc):
        assert calc("1 + 2 + 3 + 4") == 10
        assert calc("10 - 3 - 2 - 1") == 4

    def test_agrupamentos_com_parenteses(self, calc):
        calc("2 * (3 + 4)") == 14
        calc("(42)") == 42
        calc("(21 + 21) * 2") == 42

    @pytest.mark.parametrize("op1,op2", [(x, y) for x in "+-*/^" for y in "+-*/^"])
    def test_todos_os_pares_de_operadores(self, op1, op2, calc):
        src = f"1.0 {op1} 2.0 {op2} 3.0"
        res = calc(src)
        py = eval(src.replace("^", "**"))

        print("testing:", src)
        assert abs(res - py) <= 1e-9, f"{src} => {res} (esperava {py})"


class TestSubmission(TestAnswer):
    @pytest.fixture(scope="module")
    def calc(self, loader):
        return loader("precedencia").eval_calc
