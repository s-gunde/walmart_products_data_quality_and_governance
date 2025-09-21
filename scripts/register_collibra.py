# Mock Collibra integration
import json

def register_dataset(dataset_name, path):
    metadata = {
        "dataset": dataset_name,
        "path": path,
        "owner": "Data Governance Team",
        "domain": "Retail Products"
    }
    print("📡 Registering in Collibra...")
    print(json.dumps(metadata, indent=2))

if __name__ == "__main__":
    register_dataset("Walmart Sample Products", "../data/processed/walmart_sample.csv")
