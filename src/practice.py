
"""Test Yourself tasks for the Pandas lab."""

import pandas as pd


# ===== Step 1: Series and DataFrames =====

def t1_1_weather_series(df):
    """Return temp_c as a Series indexed by day names."""
    return pd.Series(df["temp_c"].values, index=df["day"].values)


def t1_2_hottest_day(df):
    """Return the name of the day with the highest temperature."""
    return df.loc[df["temp_c"].idxmax(), "day"]


def t1_3_build_frame():
    """Build and return the requested DataFrame."""
    return pd.DataFrame({
        "item": ["pen", "book", "bag"],
        "price": [10, 120, 800],
    })


def t1_4_series_vs_frame(df):
    """Return the type names of a Series and a one-column DataFrame."""
    a = type(df["temp_c"]).__name__
    b = type(df[["temp_c"]]).__name__
    return (a, b)


# ===== Step 2: Reading and writing files =====

def t2_1_csv_roundtrip(df, path):
    """Save CSV without the index, read it back, and return its shape."""
    df.to_csv(path, index=False)
    result = pd.read_csv(path)
    return result.shape


def t2_2_json_columns(df, path):
    """Save JSON with one object per row and return column names."""
    df.to_json(path, orient="records")
    result = pd.read_json(path, orient="records")
    return result.columns.tolist()


def t2_3_excel_roundtrip(df, path):
    """Save Excel without the index, read it back, and return its shape."""
    df.to_excel(path, index=False)
    result = pd.read_excel(path)
    return result.shape


def t2_4_index_trap(df, path):
    """Save CSV with the default index and return the read-back column count."""
    df.to_csv(path)
    result = pd.read_csv(path)
    return len(result.columns)


# ===== Step 3: Inspection and cleaning =====

def t3_1_count_missing(df):
    """Return missing-value counts per column as a dictionary."""
    return df.isna().sum().to_dict()


def t3_2_math_numeric(df):
    """Convert math scores to numeric and return the values as a list."""
    return pd.to_numeric(df["math"], errors="coerce").tolist()


def t3_3_remove_duplicates(df):
    """Remove duplicate rows and return the new shape."""
    return df.drop_duplicates().shape


def t3_4_fill_english_median(df):
    """Remove duplicates and fill missing English marks with the median."""
    result = df.drop_duplicates().copy()
    result["english"] = result["english"].fillna(
        result["english"].median()
    )
    return result["english"].tolist()


def t3_5_rows_after_dropna(df):
    """Clean math, remove duplicates, drop rows with remaining missing values."""
    result = df.drop_duplicates().copy()
    result["math"] = pd.to_numeric(result["math"], errors="coerce")
    result = result.dropna()
    return len(result)


def t3_6_section_category(df):
    """Convert section to category and return its dtype name."""
    result = df.copy()
    result["section"] = result["section"].astype("category")
    return result["section"].dtype.name


def t3_7_clean_students(df):
    """Fully clean the student dataset and return the cleaned DataFrame."""
    result = df.drop_duplicates().copy()

    result["math"] = pd.to_numeric(result["math"], errors="coerce")

    result["math"] = result["math"].fillna(result["math"].mean())
    result["english"] = result["english"].fillna(
        result["english"].median()
    )

    return result


# ===== Step 4: Selecting, filtering, sorting =====

def t4_1_cheap_products(df):
    """Return product names with price below 50."""
    return df.loc[df["price"] < 50, "product"].tolist()


def t4_2_accessories_in_stock(df):
    """Return Accessories product names with stock above zero."""
    mask = (df["category"] == "Accessories") & (df["stock"] > 0)
    return df.loc[mask, "product"].tolist()


def t4_3_top_two_by_price(df):
    """Return names of the two most expensive products."""
    return df.sort_values("price", ascending=False)["product"].head(2).tolist()


def t4_4_loc_price(df):
    """Return the price at index label 3 using loc."""
    return df.loc[3, "price"]


def t4_5_iloc_block(df):
    """Return the first two rows and first two columns as a list of lists."""
    return df.iloc[:2, :2].values.tolist()


def t4_6_low_stock_or_premium(df):
    """Return products with stock below 6 OR price above 500."""
    mask = (df["stock"] < 6) | (df["price"] > 500)
    return df.loc[mask, "product"].tolist()


def t4_7_sort_two_keys(df):
    """Sort category A-Z, then price highest first."""
    result = df.sort_values(
        ["category", "price"],
        ascending=[True, False],
    )
    return result["product"].tolist()


# ===== Step 5: Grouping, merging, apply =====

def t5_1_stock_by_category(products):
    """Return total stock for each category."""
    return products.groupby("category")["stock"].sum().to_dict()


def t5_2_avg_price_by_category(products):
    """Return average price per category rounded to two decimals."""
    return (
        products.groupby("category")["price"]
        .mean()
        .round(2)
        .to_dict()
    )


def t5_3_category_summary(products):
    """Return product count and maximum price per category."""
    result = products.groupby("category").agg(
        n=("product_id", "count"),
        max_price=("price", "max"),
    )
    return result.to_dict("index")


def t5_4_left_merge_names(orders, products):
    """Left-merge orders and return product names, preserving unmatched orders."""
    result = orders.merge(
        products[["product_id", "product"]],
        on="product_id",
        how="left",
    )
    return result["product"].tolist()


def t5_5_inner_merge_rows(orders, products):
    """Return the number of rows in an inner merge."""
    result = orders.merge(products, on="product_id", how="inner")
    return len(result)


def t5_6_revenue_list(orders, products):
    """Return revenue per matched order as a list."""
    result = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="inner",
    )
    return (result["qty"] * result["price"]).tolist()


def t5_7_revenue_by_customer(orders, products):
    """Return total revenue per customer, considering matched products only."""
    result = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="inner",
    )
    result["revenue"] = result["qty"] * result["price"]
    return result.groupby("customer")["revenue"].sum().to_dict()


def t5_8_price_label(products):
    """Label prices cheap, mid, or premium."""
    def label(price):
        if price < 50:
            return "cheap"
        if price < 500:
            return "mid"
        return "premium"

    return products["price"].apply(label).tolist()


def t5_9_upper_names(products):
    """Return product names in uppercase using a string method."""
    return products["product"].str.upper().tolist()


# ===== Step 6: Feature preparation =====

def t6_1_price_zscore(df):
    """Return price z-scores rounded to two decimals."""
    scores = (df["price"] - df["price"].mean()) / df["price"].std()
    return scores.round(2).tolist()


def t6_2_dummy_columns(df):
    """One-hot encode category with the cat_ prefix and integer values."""
    result = pd.get_dummies(
        df["category"],
        prefix="cat",
        dtype=int,
    )
    return result.columns.tolist()


def t6_3_feature_matrix(df):
    """Create the requested feature matrix."""
    result = df.copy()

    result["price_z"] = (
        (result["price"] - result["price"].mean())
        / result["price"].std()
    ).round(2)

    dummies = pd.get_dummies(
        result["category"],
        prefix="cat",
        dtype=int,
    )

    result = pd.concat([result, dummies], axis=1)

    result = result.drop(columns=["product_id", "product", "price"])

    return result


def t6_4_minmax_stock(df):
    """Scale stock to the 0-1 range and round to two decimals."""
    minimum = df["stock"].min()
    maximum = df["stock"].max()

    scaled = (df["stock"] - minimum) / (maximum - minimum)
    return scaled.round(2).tolist()


def t6_5_train_test_sizes(df):
    """Return the row counts for the first 80% and the remaining rows."""
    train_rows = int(len(df) * 0.8)
    test_rows = len(df) - train_rows
    return (train_rows, test_rows)


# ===== Step 7: Capstone =====

def t7_1_top_customer(orders, products):
    """Return the customer with the highest total matched revenue."""
    revenue = t5_7_revenue_by_customer(orders, products)
    return max(revenue, key=revenue.get)


def t7_2_best_selling_product(orders, products):
    """Return the product with the highest total quantity sold."""
    result = orders.merge(
        products[["product_id", "product"]],
        on="product_id",
        how="inner",
    )
    quantities = result.groupby("product")["qty"].sum()
    return quantities.idxmax()


def t7_3_customer_ranking(orders, products):
    """Return customers ranked by total revenue, highest first."""
    revenue = t5_7_revenue_by_customer(orders, products)
    return sorted(revenue, key=revenue.get, reverse=True)


def t7_4_unmatched_orders(orders, products):
    """Return order IDs whose product IDs are absent from the catalogue."""
    unmatched = ~orders["product_id"].isin(products["product_id"])
    return orders.loc[unmatched, "order_id"].tolist()


def t7_5_save_report(orders, products, path):
    """Save total revenue per customer to CSV, highest first, without index."""
    revenue = t5_7_revenue_by_customer(orders, products)

    report = pd.DataFrame({
        "customer": list(revenue.keys()),
        "revenue": list(revenue.values()),
    })

    report = report.sort_values("revenue", ascending=False)
    report.to_csv(path, index=False)
import pandas as pd


def t1_1_weather_series(df):
    return df.set_index("day")["temp_c"]


def t1_2_hottest_day(df):
    weather = df.set_index("day")
    return weather["temp_c"].idxmax()


def t1_3_build_frame():
    return pd.DataFrame({
        "Name": ["Ali", "Sara", "Ahmed"],
        "Marks": [85, 92, 78]
    })


def t1_4_series_vs_frame(df):
    return (
        type(df["temp_c"]).__name__,
        type(df[["temp_c"]]).__name__
    )
    
def t2_1_csv_roundtrip(df, path):
    """Save to CSV and read it back; return the shape."""
    df.to_csv(path, index=False)
    return pd.read_csv(path).shape


def t2_2_json_columns(df, path):
    """Save as JSON records and return the columns after reading."""
    df.to_json(path, orient="records")
    return list(pd.read_json(path).columns)


def t2_3_excel_roundtrip(df, path):
    """Save to Excel and read it back; return the shape."""
    df.to_excel(path, index=False)
    return pd.read_excel(path).shape


def t2_4_index_trap(df, path):
    """Save without specifying index=False and return the read-back columns."""
    df.to_csv(path)
    return list(pd.read_csv(path).columns)


# STEP 4: Selecting, Filtering and Sorting

def t4_1_cheap_products(df):
    """Return products with price below 50."""
    return df[df["price"] < 50]


def t4_2_accessories_in_stock(df):
    """Return accessories that have stock greater than zero."""
    return df[(df["category"] == "Accessories") & (df["stock"] > 0)]


def t4_3_top_two_by_price(df):
    """Return the two most expensive products."""
    return df.sort_values("price", ascending=False).head(2)


def t4_4_loc_price(df):
    """Return the price of the product at index label 2."""
    return df.loc[2, "price"]


def t4_5_iloc_block(df):
    """Return the first two rows and first three columns."""
    return df.iloc[0:2, 0:3]


def t4_6_low_stock_or_premium(df):
    """Return products with stock below 10 OR price above 200."""
    return df[(df["stock"] < 10) | (df["price"] > 200)]


def t4_7_sort_two_keys(df):
    """Sort by category ascending and price descending."""
    return df.sort_values(
        ["category", "price"],
        ascending=[True, False]
    )
