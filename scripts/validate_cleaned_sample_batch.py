import pandas as pd
from datetime import datetime
import great_expectations as ge
from great_expectations.checkpoint import SimpleCheckpoint

# -------------------------
# 1. Load data
# -------------------------
df = pd.read_csv("walmart_products.csv")

# -------------------------
# 2. Create Great Expectations context
# -------------------------
context = ge.get_context()

# -------------------------
# 3. Define expectation suite
# -------------------------
suite_name = "walmart_suite"
try:
    context.create_expectation_suite(suite_name, overwrite_existing=True)
except:
    pass

# Create a batch request for your dataframe
batch_request = {
    "datasource_name": "pandas_datasource",
    "data_connector_name": "default_runtime_data_connector_name",
    "data_asset_name": "walmart_products",  # logical name
    "runtime_parameters": {"batch_data": df},
    "batch_identifiers": {"default_identifier_name": "default_id"},
}

# Get a Validator to define expectations
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name
)

# -------------------------
# 4. Add expectations
# -------------------------

# Example expectations (customize as needed)
validator.expect_column_values_to_not_be_null("size")  # Fail if null
validator.expect_column_values_to_be_between("price", min_value=0)  # Price >= 0
validator.expect_column_value_lengths_to_be_between("gtin", min_value=12, max_value=14)

# Save expectations
validator.save_expectation_suite(discard_failed_expectations=False)

# -------------------------
# 5. Run Checkpoint validation
# -------------------------
checkpoint = SimpleCheckpoint(
    name="walmart_checkpoint",
    data_context=context,
    validations=[
        {
            "batch_request": batch_request,
            "expectation_suite_name": suite_name,
        }
    ],
)

results = checkpoint.run()

# -------------------------
# 6. Extract results into CSV
# -------------------------
rows = []
for res in results["run_results"].values():
    validation = res["validation_result"]
    success = validation["success"]
    stats = validation["statistics"]

    rows.append({
        "success": success,
        "evaluated_expectations": stats["evaluated_expectations"],
        "successful_expectations": stats["successful_expectations"],
        "unsuccessful_expectations": stats["unsuccessful_expectations"],
        "success_percent": stats["successful_expectations"] / max(stats["evaluated_expectations"], 1) * 100,
        "run_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

results_df = pd.DataFrame(rows)
results_df.to_csv("validation_results.csv", index=False)

print("Validation complete ✅. Results saved to validation_results.csv")
print(results_df)
