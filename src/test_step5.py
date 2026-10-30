
from src.dataset import make_products, make_orders
from src.practice import (
    t5_1_stock_by_category,
    t5_2_avg_price_by_category,
    t5_3_category_summary,
    t5_4_left_merge_names,
    t5_5_inner_merge_rows,
    t5_6_revenue_list,
    t5_7_revenue_by_customer,
    t5_8_price_label,
    t5_9_upper_names
)

products = make_products()
orders = make_orders()

print("5.1 Stock by category:")
print(t5_1_stock_by_category(products))

print("\n5.2 Average price by category:")
print(t5_2_avg_price_by_category(products))

print("\n5.3 Category summary:")
print(t5_3_category_summary(products))

print("\n5.4 Left merge:")
print(t5_4_left_merge_names(products, orders))

print("\n5.5 Inner merge:")
print(t5_5_inner_merge_rows(products, orders))

print("\n5.6 Revenue list:")
print(t5_6_revenue_list(products, orders))

print("\n5.7 Revenue by customer:")
print(t5_7_revenue_by_customer(products, orders))

print("\n5.8 Price labels:")
print(t5_8_price_label(products))

print("\n5.9 Uppercase names:")
print(t5_9_upper_names(products))
