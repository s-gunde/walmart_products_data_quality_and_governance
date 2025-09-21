import great_expectations as ge
import pandas as pd

df = pd.read_csv("../data/walmart_products_clean.csv")
gdf = ge.from_pandas(df)

# Rules
gdf.expect_column_values_to_not_be_null("gtin")
gdf.expect_column_values_to_be_unique("gtin")
gdf.expect_column_values_to_match_regex("gtin", r"^\d{12,14}$")

gdf.expect_column_values_to_be_between("price", min_value=0.01, max_value=10000)

gdf.expect_column_values_to_not_be_null("brand")
gdf.expect_column_values_to_not_be_null("category")

gdf.expect_column_value_lengths_to_be_between("product_name", 3, 200)

# Run validation
results = gdf.validate()
print(results)


import pandas as pd

df = pd.read_csv("../data/walmart_products_clean.csv")

# Rule checks
rules = {
    "GTIN Completeness": df["gtin"].notnull().mean() * 100,
    "GTIN Uniqueness": (1 - df["gtin"].duplicated().mean()) * 100,
    "Price Validity": (df["price"] > 0).mean() * 100,
    "Brand Completeness": df["brand"].notnull().mean() * 100,
    "Category Completeness": df["category"].notnull().mean() * 100,
}

print("Data Quality Report:")
for k, v in rules.items():
    print(f"{k}: {v:.2f}%")

