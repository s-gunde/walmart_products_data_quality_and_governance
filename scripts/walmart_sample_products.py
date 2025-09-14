
# Walmart Product Details 2020 - Sample Extraction Notebook
# This notebook extracts sample of 5,000 products from 30K products with GTIN, price, brand, product_name, size, category, and image URL.

import pandas as pd

# 1. Load the dataset
df = pd.read_csv("../data/walmart_product_details.csv")
print(df.head(20))

# Get rows and columns
print(df.shape)

# 2. Inspect columns
print("Columns:", df.columns)

#3. Select relevant columns 
columns_needed = ["Gtin", "Brand", "Product Name", "Description", "List Price", "Package Size", "Category", "Product Url"]
df_selected = df[columns_needed]

# 4. Drop rows with missing GTIN, product name and price 
df_selected = df_selected.dropna(subset=["Gtin", "List Price", "Product Name"])

# 5. Filter valid prices (positive numbers)
df_selected = df_selected[df_selected["List Price"] > 0]

# 6. Randomly sample 5,000 records
df_sample = df_selected.sample(n=5000, random_state=42)

# 7. Save to new CSV
df_sample.to_csv("../data/walmart_products_sample_5000.csv", index=False)
print("Sample CSV saved with 5,000 records!") 
