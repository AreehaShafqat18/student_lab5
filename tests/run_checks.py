
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
def run_step_5():
    from src.dataset import make_products, make_orders

    products = make_products()
    orders = make_orders()

    check("5.1 Stock by category", practice.t5_1_stock_by_category, products)
    check("5.2 Average price", practice.t5_2_avg_price_by_category, products)
    check("5.3 Category summary", practice.t5_3_category_summary, products)
    check("5.4 Left merge", practice.t5_4_left_merge_names, products, orders)
    check("5.5 Inner merge", practice.t5_5_inner_merge_rows, products, orders)
    check("5.6 Revenue list", practice.t5_6_revenue_list, products, orders)
    check("5.7 Revenue by customer", practice.t5_7_revenue_by_customer, products, orders)
    check("5.8 Price label", practice.t5_8_price_label, products)
    check("5.9 Uppercase names", practice.t5_9_upper_names, products)


def run_step_6():
    from src.dataset import make_products
    from src.practice import (
        t6_1_price_zscore,
        t6_2_dummy_columns,
        t6_3_feature_matrix,
        t6_4_minmax_stock,
        t6_5_train_test_sizes
    )

    df = make_products()

    check("6.1 Price z-score", lambda: t6_1_price_zscore(df))
    check("6.2 Dummy columns", lambda: t6_2_dummy_columns(df))
    check("6.3 Feature matrix", lambda: t6_3_feature_matrix(df))
    check("6.4 Min-max stock", lambda: t6_4_minmax_stock(df))
    check("6.5 Train/test sizes", lambda: t6_5_train_test_sizes(df))
    
def run_step_7():
    from src.dataset import make_orders, make_products
    from src.practice import (
        t7_1_top_customer,
        t7_2_best_selling_product,
        t7_3_customer_ranking,
        t7_4_unmatched_orders,
        t7_5_save_report
    )

    orders = make_orders()
    products = make_products()

    check("7.1 Top customer", lambda: t7_1_top_customer(orders, products))
    check("7.2 Best-selling product", lambda: t7_2_best_selling_product(orders, products))
    check("7.3 Customer ranking", lambda: t7_3_customer_ranking(orders, products))
    check("7.4 Unmatched orders", lambda: t7_4_unmatched_orders(orders, products))
    check("7.5 Save report", lambda: t7_5_save_report(orders, products, "results/report.csv"))



def main():
    if len(sys.argv) < 2:
        steps = ["2", "3", "4", "5", "6", "7"]
    else:
        steps = [sys.argv[1]]

    for step in steps:
        if step == "2":
            run_step_2()
        elif step == "3":
            run_step_3()
        elif step == "4":
            run_step_4()
        elif step == "5":
            run_step_5()
        elif step == "6":
            run_step_6()
        elif step == "7":
            run_step_7()
        else:
            print(f"Step {step} is not implemeted.")
if __name__ == "__main__":
    main()