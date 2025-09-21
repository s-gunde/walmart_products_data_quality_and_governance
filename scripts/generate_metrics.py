import pandas as pd

def generate_metrics(file_path, output_path):
    df = pd.read_csv(file_path)
    metrics = {
        "rows": len(df),
        "missing_brand": df['brand'].isna().mean() * 100,
        "invalid_price": (df['price'] <= 0).mean() * 100,
        "unique_categories": df['category'].nunique()
    }
    pd.DataFrame([metrics]).to_csv(output_path, index=False)
    print(f"📊 Metrics saved to {output_path}")

if __name__ == "__main__":
    generate_metrics("../data/processed/walmart_sample.csv",
                     "../data/processed/quality_metrics.csv")
