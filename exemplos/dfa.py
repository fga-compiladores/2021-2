from dataclasses import dataclass


@dataclass()
class DFA:
    transition: dict
    accepts: set
    start: str

    def accept(self, src: str) -> bool:
        st = self.start
        for c in src:
            try:
                st = self.transition[st][c]
            except KeyError:
                return False
        return st in self.accepts

    def match(self, src: str) -> str:
        st = self.start
        final_pos = None
        for i, c in enumerate(src):
            try:
                st = self.transition[st][c]
                if st in self.accepts:
                    final_pos = i + 1
            except KeyError:
                break

        if final_pos is None:
            return None
        else:
            return src[:final_pos]


dfa_ex = DFA(
    transition={
        "A": {"0": "B", "1": "C"},
        "B": {},
        "C": {"0": "D", "1": "C"},
        "D": {"0": "D", "1": "C"},
    },
    accepts={"B", "D"},
    start="A",
)


if __name__ == "__main__":
    while True:
        st = input("st: ")
        if st == "":
            break
        print(dfa_ex.match(st))
