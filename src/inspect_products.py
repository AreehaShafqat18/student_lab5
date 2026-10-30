
from src.dataset import make_products

products = make_products()

print("PRODUCT DATA:")
print(products)

print("\nCOLUMN NAMES:")
print(products.columns.tolist())

print("\nINDEX LABELS:")
print(products.index.tolist())
