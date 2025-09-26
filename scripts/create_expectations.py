import great_expectations as gx
import pandas as pd
from great_expectations.core.batch import RuntimeBatchRequest

# Load Walmart dataset
df = pd.read_csv("../data/walmart_products_cleaned_5000.csv")

# Get GX context
context = gx.get_context()

# ------------------------
# 1️⃣ Ensure a Pandas datasource exists
# ------------------------
datasource_name = "my_pandas_datasource"
connector_name = "default_runtime_data_connector_name"

if not context.list_datasources():
    context.add_datasource(
        name=datasource_name,
        class_name="Datasource",
        execution_engine={"class_name": "PandasExecutionEngine"},
        data_connectors={
            connector_name: {
                "class_name": "RuntimeDataConnector",
                "batch_identifiers": ["default_identifier_name"],
            }
        },
    )
    print(f"Datasource '{datasource_name}' created.")
else:
    # Use existing datasource
    datasource_name = context.list_datasources()[0]["name"]
    connector_name = list(context.datasources[datasource_name].data_connectors.keys())[0]
    print(f"Using existing datasource '{datasource_name}' and connector '{connector_name}'")

# ------------------------
# 2️⃣ Create or overwrite expectation suite
# ------------------------
suite_name = "walmart_product_suite"
context.add_or_update_expectation_suite(expectation_suite_name=suite_name)

# ------------------------
# 3️⃣ Create validator
# ------------------------
batch_request = RuntimeBatchRequest(
    datasource_name=datasource_name,
    data_connector_name=connector_name,
    data_asset_name="walmart_data",
    runtime_parameters={"batch_data": df},
    batch_identifiers={"default_identifier_name": "default_identifier"},
)

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name,
)

# ------------------------
# 4️⃣ Add expectations
# ------------------------
validator.expect_column_values_to_not_be_null("Gtin")
validator.expect_column_values_to_match_regex("Gtin",  r"^\d{12}$")
validator.expect_column_values_to_be_unique("Gtin")

validator.expect_column_values_to_not_be_null("Brand")
validator.expect_column_value_lengths_to_be_between("Brand", min_value=2, max_value=50)

validator.expect_column_values_to_not_be_null("Product Name")
validator.expect_column_value_lengths_to_be_between("Product Name", min_value=3, max_value=200)

validator.expect_column_values_to_not_be_null("List Price")
validator.expect_column_values_to_be_between("List Price", min_value=0.5, max_value=5000)

validator.expect_column_values_to_not_be_null("Size")
validator.expect_column_values_to_not_be_null("Category")
validator.expect_column_values_to_be_unique("Category")

# ------------------------
# 5️⃣ Save expectation suite
# ------------------------
validator.save_expectation_suite(discard_failed_expectations=False)
print(f"Expectation suite '{suite_name}' created successfully!")
