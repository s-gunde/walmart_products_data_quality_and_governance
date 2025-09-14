import pandas as pd
import requests
import time

INPUT_FILE = "data/retail_products.csv"
OUTPUT_FILE = "data/retail_products_with_images.csv"

def fetch_image_url(gtin):
    """Fetch image URL from Open Food Facts API, else return placeholder."""
    gtin_str = str(gtin).zfill(13)
    api_url = f"https://world.openfoodfacts.org/api/v0/product/{gtin_str}.json"

    try:
        resp = requests.get(api_url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if "product" in data and "image_url" in data["product"]:
                return data["product"]["image_url"]
    except Exception as e:
        print(f"Error fetching GTIN {gtin}: {e}")

    # Fallback placeholder (always valid)
    return f"https://picsum.photos/200?random={gtin_str}"

def main():
    print("Loading dataset...")
    df = pd.read_csv(INPUT_FILE)

    print("Updating image URLs...")
    df["image_url"] = df["gtin"].apply(fetch_image_url)

    print(f"Saving updated dataset to {OUTPUT_FILE}...")
    df.to_csv(OUTPUT_FILE, index=False)

    print("✅ Done! All image URLs updated.")

if __name__ == "__main__":
    main()
