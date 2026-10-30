
from src.dataset import make_products, make_orders

products = make_products()
orders = make_orders()

print("PRODUCTS DATA:")
print(products)

print("\nORDERS DATA:")
print(orders)

print("\nPRODUCT COLUMNS:")
print(products.columns.tolist())

print("\nORDERS COLUMNS:")
print(orders.columns.tolist())
