from types import SimpleNamespace
import pytest
from pathlib import Path
from types import SimpleNamespace
import os


@pytest.fixture(scope="session")
def path():
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def floader(path):
    def floader(name, skip=None):
        only_ans = os.environ.get("ANSWER", "false").lower() == "true"
        if only_ans and "answer" not in str(name):
            pytest.skip(f"not an anwser module: {name}")
        try:
            with open(path / name) as fd:
                return fd.read()
        except FileNotFoundError:
            skip = skip.format(name=name) if skip else f"path not found: {name}"
            pytest.skip(skip)

    return floader


@pytest.fixture(scope="session")
def loader(floader):
    def loader(name, skip=None):
        filename = name + ".py"
        src = floader(filename, skip)
        code = compile(src, filename, "exec")
        ns = {}
        exec(code, ns, ns)
        return SimpleNamespace(**ns)

    return loader
