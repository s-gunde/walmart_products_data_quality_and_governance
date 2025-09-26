import great_expectations as gx
import pandas as pd

# Load dataset
df = pd.read_csv("../data/walmart_products_cleaned_5000.csv")

# Get context and suite
context = gx.get_context()
suite_name = "walmart_product_suite"

# Convert dataframe into GX batch
batch = gx.dataset.PandasDataset(df)
suite = context.get_expectation_suite(suite_name)

# Validate
results = batch.validate(expectation_suite=suite)

# Save HTML report
validation_result_identifier = context.run_validation_operator(
    "action_list_operator",
    assets_to_validate=[batch]
)

context.build_data_docs()
context.open_data_docs()

print("Validation completed. Check gx_reports/ for HTML report.")
