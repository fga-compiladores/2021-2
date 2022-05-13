import pytest
import re

part1 = re.compile(r"^[a-f]\)\s+?[AB]+:\s+([^\n]+)", flags=re.MULTILINE)
part2 = re.compile(r"(G[1-6])\)([^\n]+)")


class TestSubmission:
    @pytest.fixture(scope="module")
    def ans(self, floader):
        msg = "Precisa rodar no computador do professor ;)"
        return floader("gramaticas.answer.md", skip=msg)

    @pytest.fixture(scope="module")
    def src(self, floader):
        return floader("gramaticas.md")

    def get_examples(self, src):
        def f(st):
            st = st.strip()
            if st == "ε":
                return set()
            return {x.strip() for x in st.split(",")}

        return [f(m.group(1)) for m in part1.finditer(src)]

    def get_descriptions(self, src):
        res = {}
        for m in part2.finditer(src):
            descr = m.group(2).strip()
            if descr != "...":
                res[m.group(1)] = descr
        return res

    def check_part_1(self, ans, src):
        expect = self.get_examples(ans)
        got = self.get_examples(src)
        errors = []
        for x, y, name in zip(expect, got, "abcdefgh"):
            if x != y:
                errors.append(f"erro em {name}. got: {y}, expect: {x}")
        return errors

    def test_part_1(self, ans, src):
        errors = self.check_part_1(ans, src)
        for error in errors:
            print(error)
        assert not errors

    def test_conseguiu_1pt(self, ans, src):
        num_errors = len(self.check_part_1(ans, src))
        assert num_errors <= 6

    def test_conseguiu_2pts(self, ans, src):
        num_errors = len(self.check_part_1(ans, src))
        assert num_errors <= 4

    def test_conseguiu_3pts(self, ans, src):
        num_errors = len(self.check_part_1(ans, src))
        assert num_errors <= 2

    def test_conseguiu_4pts(self, ans, src):
        num_errors = len(self.check_part_1(ans, src))
        assert num_errors == 0

    def test_part_2(self, ans, src):
        expect = self.get_descriptions(ans)
        got = self.get_descriptions(src)
        assert set(got) == set(expect), "Não respondeu a todas as questões"

        print("Iniciando a correção manual\n")
        for key, descr in expect.items():
            print(key)
            print("  - Gabarito:", descr)
            print("  - Resposta:", got[key])
            if not self.get_yn("Correto? "):
                assert False, "TODAS descrições devem estar corretas!"
