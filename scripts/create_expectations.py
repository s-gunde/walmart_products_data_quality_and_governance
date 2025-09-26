import great_expectations as gx
import pandas as pd

# Load dataset
df = pd.read_csv("../data/walmart_products_cleaned_5000.csv")

# Suite name
suite_name = "walmart_product_suite"

# Create validator directly from pandas DataFrame (no expectation_suite_name here)
validator = gx.from_pandas(df)

# Attach an expectation suite to it
validator.create_expectation_suite(suite_name, overwrite_existing=True)

# GTIN rules
validator.expect_column_values_to_not_be_null("Gtin")
validator.expect_column_values_to_match_regex("Gtin", r"^\d{12,14}$")
validator.expect_column_values_to_be_unique("Gtin")

# Brand rules
validator.expect_column_values_to_not_be_null("Brand")
validator.expect_column_value_lengths_to_be_between("Brand", min_value=2, max_value=50)

# Name rules
validator.expect_column_values_to_not_be_null("Product Name")
validator.expect_column_value_lengths_to_be_between("Product Name", min_value=3, max_value=200)

# Price rules
validator.expect_column_values_to_not_be_null("List Price")
validator.expect_column_values_to_be_between("List Price", min_value=0.5, max_value=5000)

# Size rules
validator.expect_column_values_to_not_be_null("Size")

# Category rules
validator.expect_column_values_to_not_be_null("Category")

# Save the suite
validator.save_expectation_suite(discard_failed_expectations=False)

print(f"Expectation suite '{suite_name}' created successfully!")
