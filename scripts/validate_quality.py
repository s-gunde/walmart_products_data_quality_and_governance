import great_expectations as ge

def validate_data(file_path):
    df = ge.read_csv(file_path)

    results = {
        "gtin_format": df.expect_column_values_to_match_regex("gtin", r"^\d{8,14}$"),
        "price_valid": df.expect_column_values_to_be_between("price", min_value=0.1, max_value=10000),
        "brand_not_null": df.expect_column_values_to_not_be_null("brand"),
        "category_valid": df.expect_column_values_to_be_in_set(
            "category", ["Grocery", "Health", "Electronics", "Clothing", "Household"]
        ),
    }
    for k, v in results.items():
        print(f"{k}: {v['success']}")
    return results

if __name__ == "__main__":
    validate_data("../data/processed/walmart_sample.csv")
