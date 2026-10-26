
import sys
import tempfile
from pathlib import Path

import pandas as pd

from src import practice
from src.dataset import make_products, make_weather


def check(task_name, function, *args):
    try:
        function(*args)
        print(f"PASS {task_name} (function executed)")
    except Exception as exc:
        print(f"FAIL {task_name}: {exc}")


def run_step_2():
    products = make_products()

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)

        check(
            "2.1 CSV roundtrip",
            practice.t2_1_csv_roundtrip,
            products,
            str(temp / "data.csv"),
        )
        check(
            "2.2 JSON columns",
            practice.t2_2_json_columns,
            products,
            str(temp / "data.json"),
        )
        check(
            "2.3 Excel roundtrip",
            practice.t2_3_excel_roundtrip,
            products,
            str(temp / "data.xlsx"),
        )
        check(
            "2.4 Index trap",
            practice.t2_4_index_trap,
            products,
            str(temp / "_tmp_b.csv"),
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m tests.run_checks 2")
        return

    step = sys.argv[1]

    if step == "2":
        run_step_2()
    else:
        print(f"Step {step} is not implemented in this checker.")


if __name__ == "__main__":
    main()
