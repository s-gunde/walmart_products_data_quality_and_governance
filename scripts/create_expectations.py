import great_expectations as gx
import pandas as pd

# Load dataset
df = pd.read_csv("../data/walmart_products_cleaned_5000.csv")

# Create Great Expectations context (local filesystem)
context = gx.get_context()

# Create Expectation Suite
suite_name = "walmart_product_suite"
try:
    suite = context.create_expectation_suite(suite_name, overwrite_existing=True)
except:
    suite = context.get_expectation_suite(suite_name)

# Convert pandas df to GX dataset
batch = gx.dataset.PandasDataset(df)

# GTIN rules
batch.expect_column_values_to_not_be_null("Gtin")
batch.expect_column_values_to_match_regex("Gtin", r"^\d{12,14}$")
batch.expect_column_values_to_be_unique("Gtin")

# Brand rules
batch.expect_column_values_to_not_be_null("Brand")
batch.expect_column_value_lengths_to_be_between("Brand", min_value=2, max_value=50)

# Name rules
batch.expect_column_values_to_not_be_null("Product Name")
batch.expect_column_value_lengths_to_be_between("Product Name", min_value=3, max_value=200)

# Price rules
batch.expect_column_values_to_not_be_null("List Price")
batch.expect_column_values_to_be_between("List Price", min_value=0.5, max_value=5000)

# Size rules
batch.expect_column_values_to_not_be_null("Size")

# Category rules
batch.expect_column_values_to_not_be_null("Category")

# Save suite
context.save_expectation_suite(batch.get_expectation_suite(), suite_name)
print(f"Expectation suite '{suite_name}' created.")
