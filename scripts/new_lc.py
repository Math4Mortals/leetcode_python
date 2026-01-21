from __future__ import annotations
from textwrap import dedent

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def create_title(title: str) -> str:
    title = title.strip().lower()
    title = re.sub(r"[^a-z0-9]+", "_", title)
    title = re.sub(r"_+", "_", title).strip("_")
    return title or "problem"

def main() -> int:
    if len(sys.argv) < 3:
        print('Usage: python scripts/new_lc.py <number> "<title>" [difficulty]')
        print('Example: python scripts/new_lc.py 88 "merge sorted array" easy')
        return 2

    num = int(sys.argv[1])
    title = sys.argv[2]
    difficulty = (sys.argv[3] if len(sys.argv) >= 4 else "easy").lower()
    if difficulty not in {"easy", "medium", "hard"}:
        print("difficulty must be one of: easy, medium, hard")
        return 2

    lc_name = create_title(title)
    lc = f"LC{num:04d}_{lc_name}"

    sol_dir = ROOT / "solutions" / difficulty
    test_dir = ROOT / "tests"
    sol_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)

    sol_path = sol_dir / f"{lc}.py"
    test_path = test_dir / f"test_{lc}.py"

    if sol_path.exists() or test_path.exists():
        print("Already exists:")
        if sol_path.exists():
            print(f" - {sol_path}")
        if test_path.exists():
            print(f" - {test_path}")
        return 1

    sol_path.write_text(
        dedent(f"""\
    class Solution:
        # TODO: implement LeetCode method here
        pass
    """),
        encoding="utf-8",
        newline="\n",
)

    test_path.write_text(
        dedent(f"""\
    import pytest

    from solutions.{difficulty}.{lc} import Solution


    SOLUTIONS = [
        Solution,
    ]


    @pytest.mark.parametrize("args, expected", [
        # ((), None),
    ])
    @pytest.mark.parametrize("SolutionCls", SOLUTIONS)
    def test_{lc.lower()}(SolutionCls, args, expected):
        pytest.skip("TODO: implement tests")
    """),
        encoding="utf-8",
        newline="\n",
    )

    print(f"Created: {sol_path}")
    print(f"Created: {test_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())