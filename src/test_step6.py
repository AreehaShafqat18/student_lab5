
from src.dataset import make_products
from src.practice import (
    t6_1_price_zscore,
    t6_2_dummy_columns,
    t6_3_feature_matrix,
    t6_4_minmax_stock,
    t6_5_train_test_sizes
)

products = make_products()

print("6.1 Price z-score:")
print(t6_1_price_zscore(products))

print("\n6.2 Dummy columns:")
print(t6_2_dummy_columns(products))

print("\n6.3 Feature matrix:")
print(t6_3_feature_matrix(products))

print("\n6.4 Min-max stock:")
print(t6_4_minmax_stock(products))

print("\n6.5 Train and test sizes:")
print(t6_5_train_test_sizes(products))

