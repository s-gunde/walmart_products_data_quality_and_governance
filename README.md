# 🛒 Retail Data Quality & Governance

This portfolio project demonstrates **data quality** and **data governance** practices on a simulated **retail catalog dataset** (~5,000 rows).  
It is designed to showcase skills relevant to **retail/e-commerce companies** such as **Walmart, Instacart, and Loblaw**, where managing large product catalogs and ensuring high-quality data is critical.

---

## 📂 Dataset Overview

**File:** `data/retail_products.csv`  

**Rows:** ~5,000 SKUs 

**Columns:**

| Column         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `gtin`         | Global Trade Item Number (8, 12, 13, or 14 digits). Unique identifier for retail products. |
| `brand`        | Brand/manufacturer of the product (e.g., Kellogg’s, Nestlé, Unilever).      |
| `product_name` | Human-readable product title (e.g., *Coca-Cola Zero Sugar 355ml*).          |
| `size`         | Pack or unit size (e.g., `355ml`, `500g`, `12oz`, `2L`).                    |
| `category`     | Product category (e.g., Beverages, Snacks, Personal Care).                  |
| `image_url`    | Link to product image (simulated, public-safe placeholder images).           |
| `source`       | Indicates the source system (`mock_walmart`, `mock_instacart`, etc.).       |


📌 **Why this dataset?**  
This structure mirrors real catalog data in retail giants. It supports **data quality checks** (e.g., GTIN validation, null checks) and **governance workflows** (mapping attributes to a business glossary in Collibra, building KPIs in Tableau).

---

## ⚡ Features

### 🔍 Data Quality
- **Great Expectations** validations:
  - ✅ **GTIN**: Must be numeric, 8/12/13/14 characters, unique   
  - ✅ **Brand**: Cannot be null, max length 100 
  - ✅ **Product Name**: Cannot be null, meaningful length (> 3 chars)  
  - ✅ **Size**: Should follow valid unit patterns (g, ml, oz, L)
  - ✅ **Category**: Should map to controlled vocabulary (governed taxonomy)  
  - ✅ **Image URL**: Must be a valid link (`http`/`https`)  

### 📊 Exploratory Analysis
- **Jupyter Notebook** (`notebooks/exploratory_analysis.ipynb`) profiling:
  - Missing values per column  
  - Duplicate detection  
  - Top categories and brands  
  - GTIN length distribution  

### 🏢 Governance Simulation
- **Collibra Integration** (`docs/collibra_integration.md`):
  - Map dataset columns to governed assets (e.g., GTIN → Global Trade Item)  
  - Assign stewardship & ownership  
  - Use Great Expectations JSON as **data quality evidence**  
  - Simulate lineage: *Raw data → Quality checks → Business dashboards*  

### 📈 Tableau Dashboard
- Upload dataset to **Tableau Public**  
- Build KPI visualizations:  
  - % valid GTINs  
  - % missing values  
  - Top brands & categories  
- Embed Tableau link in portfolio for visibility

### :rocket: Workflow 

1. Run `notebooks/exploratory_analysis.ipynb` for initial profiling  
2. Execute `scripts/run_data_quality_checks.py` → generates `validation_results.json`  
3. Upload metadata & quality results to Collibra for governance  
4. Visualize quality KPIs in Tableau  

### 📡 Data Source & License

This dataset is **curated from fully public sources** for portfolio/demo purposes:  

- **[Open Food Facts](https://world.openfoodfacts.org/)** (primary source)  
  - Open, crowdsourced food product database  
  - Provides GTIN, brand, product name, size, categories, and images  
  - Licensed under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/)  

Additional supplemental product metadata comes from **other open datasets** (e.g., Kaggle/UCI) to balance categories and maintain a retail-like schema.  

---

## 📂 Project Structure

```bash
retail-data-quality-portfolio/
│── data/
│   └── retail_products.csv
│
│── expectations/
│   └── validation_results.json   # JSON quality report
│
│── notebooks/
│   └── exploratory_analysis.ipynb
│
│── scripts/
│   └── run_data_quality_checks.py
│
│── docs/
│   └── collibra_integration.md
│
│── README.md


