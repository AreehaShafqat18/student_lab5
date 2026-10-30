
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

print("7.1 Top customer:")
print(t7_1_top_customer(orders, products))

print("\n7.2 Best-selling product:")
print(t7_2_best_selling_product(orders, products))

print("\n7.3 Customer ranking:")
print(t7_3_customer_ranking(orders, products))

print("\n7.4 Unmatched orders:")
print(t7_4_unmatched_orders(orders, products))

print("\n7.5 Save report:")
print(t7_5_save_report(orders, products, "results/report.csv"))
