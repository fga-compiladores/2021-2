from typing import Any
import evil_module


def evil(x: Any) -> str:
    return str(x)


if __name__ == "__main__":
    print(repr(evil(42)))
    print(repr(evil(666)))
    print(repr(evil("Hello World")))
