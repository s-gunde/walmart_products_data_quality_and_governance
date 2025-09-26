import great_expectations as gx
import pandas as pd
from great_expectations.core.batch import RuntimeBatchRequest
from datetime import datetime
import os
import webbrowser

# Load dataset
df = pd.read_csv("../data/walmart_products_cleaned_5000.csv")

# GX context
context = gx.get_context()
suite_name = "walmart_product_suite"

# Datasource and connector
datasource_name = context.list_datasources()[0]["name"]
connector_name = list(context.datasources[datasource_name].data_connectors.keys())[0]

# RuntimeBatchRequest
batch_request = RuntimeBatchRequest(
    datasource_name=datasource_name,
    data_connector_name=connector_name,
    data_asset_name="walmart_data",
    runtime_parameters={"batch_data": df},
    batch_identifiers={"default_identifier_name": "default_identifier"}
)

# Validator
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name
)

# Validate
results = validator.validate()

# ------------------------
# Console summary
# ------------------------
print("\n=== VALIDATION SUMMARY ===")
print(f"Validation success: {results.success}")
print(f"Number of expectations: {len(results.results)}")

for r in results.results:
    if not r.success:
        col = r.expectation_config.kwargs.get("column")
        print(f"\nExpectation failed: {r.expectation_config.expectation_type}")
        print(f"Column: {col}")
        print(f"Observed: {r.result.get('unexpected_list', [])[:10]}")  # first 10 unexpected values

# ------------------------
# Save validation summary as CSV
# ------------------------
summary = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for r in results.results:
    col = r.expectation_config.kwargs.get("column")
    exp_type = r.expectation_config.expectation_type
    success = r.success
    unexpected_count = r.result.get("unexpected_count", 0)
    element_count = r.result.get("element_count", None)
    success_rate = r.result.get("success_percent", None)
    
    summary.append({
        "timestamp": timestamp,
        "column": col,
        "expectation_type": exp_type,
        "success": success,
        "unexpected_count": unexpected_count,
        "total_count": element_count,
        "success_rate": success_rate
    })

summary_df = pd.DataFrame(summary)

# Ensure data folder exists
os.makedirs("../data", exist_ok=True)
csv_file = "../data/walmart_validation_summary.csv"
summary_df.to_csv(csv_file, index=False)
print(f"\nValidation summary saved to {csv_file}")

# ------------------------
# Build and open Data Docs
# ------------------------
context.build_data_docs()
urls = context.open_data_docs()
print("Data Docs opened:", urls)
