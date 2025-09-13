import pandas as pd

# Load your CSV
df = pd.read_csv("data/retail_products.csv")

# Function to generate Open Food Facts image URL from GTIN
def get_off_image_url(gtin):
    # Open Food Facts uses URL pattern: https://static.openfoodfacts.org/images/products/<gtin_first_3>/<gtin_rest>/front_fr.6.400.jpg
    # GTIN needs to be zero-padded to 13 digits if shorter
    gtin_str = str(gtin).zfill(13)
    folder1 = gtin_str[:3]
    folder2 = gtin_str[3:6]
    folder3 = gtin_str[6:9]
    return f"https://static.openfoodfacts.org/images/products/{folder1}/{folder2}/{folder3}/{gtin_str}/front_fr.6.400.jpg"

# Replace placeholder URLs with Open Food Facts images
df['image_url'] = df['gtin'].apply(get_off_image_url)

# Save updated CSV
df.to_csv("data/retail_products_images_updated.csv", index=False)

print("✅ Updated CSV with real Open Food Facts image URLs saved as 'retail_products_images_updated.csv'")
