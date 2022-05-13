import tt
import re
import shutil
import subprocess
from warnings import warn
from typing import Pattern
from pathlib import Path

import pandas as pd
from rich.console import Console

TEST_RESULT: Pattern = re.compile(
    r"""
    (?:tests?\/)?                               # optional "tests/"
    test_(?P<id>[\w_-]+)\.py\s+                 # competency from file name
    (?P<result>[^\s]+)\s+                       # result string
    (?:\[\s+\d+%\])                             # completion
    """,
    flags=re.VERBOSE,
)
console = Console()


def process_pytest(path: Path, force=False) -> dict[str, float]:
    results_path = path.joinpath("pytest.out")
    if results_path.exists() and not force:
        data = results_path.read_text()
    else:
        copy_tests(path.parent.parent.joinpath("questions"), path)
        cmd = ["pytest", "--tb=no"]
        console.print(f"[yellow]*[/] testing [b]{path.name}[/]...", end="")
        result = subprocess.run(cmd, cwd=path, capture_output=True, text=True)
        console.print(f"  [b green]done![/]")
        data = result.stdout
        results_path.write_text(data)
    return parse_pytest(data)


def copy_tests(from_path: Path, to_path: Path):
    # Copy test directory
    from_tests = from_path.joinpath("tests").resolve()
    to_tests = to_path.joinpath("tests").resolve()

    if not from_tests.exists():
        warn(f'No tests found in "{from_path}"')
        return

    shutil.rmtree(to_tests, ignore_errors=True)
    shutil.copytree(from_tests, to_tests)

    # Copy answer files
    for src in from_path.iterdir():
        if ".answer." in src.name:
            dest = to_path.joinpath(src.name)
            shutil.copy(src, dest)


def parse_pytest(src: str) -> dict[str, float]:
    grades = {}
    for m in TEST_RESULT.finditer(src):
        grp = m.groupdict()
        ref = grp["id"].replace("_", "-")
        grades[ref] = parse_progress(grp["result"])
    return grades


def parse_progress(src: str) -> float:
    e = 1e-100
    src = src.replace("F", "E")
    error = src.count("E")
    passed = src.count(".")
    if passed + error == 0:
        return float("nan")
    return passed / (passed + error + e)


def main(force: bool = False, out: str = ""):
    db = {}
    sub_base = Path("submissions").resolve()
    for sub_dir in sub_base.iterdir():
        if not sub_dir.is_dir():
            continue
        grades = process_pytest(sub_dir, force=force)
        gh_id = sub_dir.name
        db[gh_id] = grades

    df = pd.DataFrame.from_records(db).T
    df.index.name = "github_id"
    if out:
        tt.save_table(df, out)
    else:
        console.print(df)


if __name__ == "__main__":
    from sidekick.app.cli import run

    run(main)
