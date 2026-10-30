
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


def run_step_3():
    from src.dataset import make_students

    df = make_students()

    check("3.1 Count missing", practice.t3_1_count_missing, df)
    check("3.2 Convert math", practice.t3_2_math_numeric, df)
    check("3.3 Remove duplicates", practice.t3_3_remove_duplicates, df)
    check("3.4 Fill English median", practice.t3_4_fill_english_median, df)
    check("3.5 Rows after dropna", practice.t3_5_rows_after_dropna, df)
    check("3.6 Section category", practice.t3_6_section_category, df)
    check("3.7 Clean students", practice.t3_7_clean_students, df)
    
    
def run_step_4():
    from src.dataset import make_products

    products = make_products()

    check("4.1 Cheap products", practice.t4_1_cheap_products, products)
    check("4.2 Accessories in stock", practice.t4_2_accessories_in_stock, products)
    check("4.3 Top two by price", practice.t4_3_top_two_by_price, products)
    check("4.4 loc price", practice.t4_4_loc_price, products)
    check("4.5 iloc block", practice.t4_5_iloc_block, products)
    check("4.6 Low stock or premium", practice.t4_6_low_stock_or_premium, products)
    check("4.7 Sort by two keys", practice.t4_7_sort_two_keys, products)



def main():
    if len(sys.argv) < 2:
        print("Usage: python -m tests.run_checks 2")
        return

    step = sys.argv[1]

    if step == "2":
        run_step_2()
    elif step == "3":
        run_step_3()
    elif step == "4":
        run_step_4()
    else:
        print(f"Step {step} is not implemented in this checker.")


if __name__ == "__main__":
    main()
