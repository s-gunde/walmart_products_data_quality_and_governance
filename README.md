# Retail Data Quality & Governance 🛒

## Project Overview
The project analyzes **real-time Walmart USA retail data**, focusing on price distributions, product
categories, and data quality improvements and to understand how Walmart prices its vast product catalog.

This project simulates how a **retail data governance pipeline** might look in such an enterprise setting.  


This project integrates:  
- Exploratory Data Analysis (EDA)
- Data Cleaning & Validation
- Great Expectations for Automated Data Quality Checks
- Collibra for Enterprise Data Governance
- Tableau Dashboard for Data Quality Metrics



---
## About Walmart USA  

- **Walmart Inc.** is the world’s largest retailer, headquartered in Bentonville, Arkansas, USA.  
- In **2024**, Walmart generated **$648 billion in revenue** globally, with the **majority from U.S. retail operations**.  
- Walmart operates **4,600+ stores in the U.S.** and is known for its **massive product catalog** of groceries, apparel, electronics, health, and household goods.  
- Walmart’s data is unique due to:  
  - **Billions of SKUs** across thousands of categories.  
  - **Rich product metadata** (GTIN, Brand, Category, Price, Size, Images).  
  - **Real-time updates** across stores and e-commerce.  
  - **High-frequency transactions** (millions per day).  
- Managing **data quality at Walmart-scale** is mission-critical for supply chain efficiency, customer experience, and financial reporting.  
---



## Step 1: Exploratory Data Analysis
- Profiled 5K Walmart product records.  
- Identified issues: missing GTINs, invalid prices, duplicate products, inconsistent brand/category labels.  
- Created visual summaries (price distribution, brand/category breakdowns).
             
   - **Brand Coverage** – top 5 brands across bins.  
   - **Category Analysis** – most common categories.  
   - **Missing Values** – % missing GTINs, Brands, Prices.  
   - **Outliers** – extreme prices beyond $2000 flagged.
   - **Price Distribution** across ranges (0–2000 USD). 
 

---

## Step 2: Data Cleaning
- Removed duplicates and invalid GTINs.  
- Normalized brand/category casing.  
- Filtered out products with missing or invalid prices.  
- Output: **clean dataset** ready for validation.

---

## Step 3: Data Validation (Great Expectations)
- Automated rules:
  - GTIN → not null, unique, 12 digits.  
  - Price → > 0 and < 5,000.  
  - Brand & Category → not null.  
  - Product Name → length 3–200 chars.  
- Generated **HTML validation docs** for transparency.

---

## Step 4: Data Governance (Collibra)
- Built a **data dictionary** defining key fields (GTIN, Price, Brand, Category).  
- Linked business policies (e.g., “Price must be > 0”) to technical rules in Great Expectations.  
- Demonstrated **lineage** from raw → cleaned → validated → dashboard.

    - **Business Glossary** – GTIN, Brand, Price, Category definitions.
    - **Policies & Standards** – e.g., 98% GTIN validity, <1% missing brands.
    - **Data Lineage** – Raw Walmart data → Cleaning → Validation → Dashboard.
    - **Issue Management** – Track exceptions like invalid GTINs or missing categories.

---

## Step 5: Dashboard
An interactive dashboard with:
- **KPI Cards**: Completeness %, Valid Prices %, Overall Data Quality Score.  
- **Failures by Rule**: Which rules fail most often.   
- **Price Outlier Detection**.  
- **Quality Trend Over Time**.

This dashboard simulates how retail stakeholders track **catalog health** and prioritize fixes.

---

## Tools & Tech
- **Python** → EDA, cleaning, validation.  
- **Great Expectations** → automated quality checks.  
- **Collibra** → data governance policies & dictionary.    

---

## Impact
This project demonstrates:
- **Data Engineering** → building pipelines for validation.  
- **Data Governance** → linking technical rules with business policies.  
- **Data Visualization** → translating quality into business KPIs.  
###  Key Takeaways
     - Real-world Walmart USA retail dataset used.
     - End-to-end governance pipeline → EDA → Cleaning → Validation → Governance → Dashboard.
     - Enterprise tools simulated: Great Expectations + Collibra + Tableau.
     - Communicates data quality to business stakeholders clearly.

---

## Data Source & License

- Walmart Product Details 2020 — [Kaggle](https://www.kaggle.com/datasets/promptcloud/walmart-product-details-2020) 

---

### Impact Story

I built a **Retail Data Quality and Governance** project using Walmart product data. I started with **EDA to profile issues**, then enforced rules using **Great Expectations**. I connected these rules to business policies in **Collibra** and finally **created charts** to see failure trends that shows data quality KPIs in real time. This project simulates how companies like Instacart or Walmart monitor catalog health and aligns perfectly with data engineering + governance roles.

---

## 📂 Project Structure

```bash

walmart-data-quality-project/
│
│── data/
│   ├── walmart_product_details.csv       # Raw source dataset
│   ├── walmart_products_sample.csv       # Sample for quick testing
│   ├── walmart_products_cleaned.csv      # Cleaned version after preprocessing
│   └── walmart_validation_summary.csv    # Validation results (CSV summary)
│
│── expectations/
│   └── walmart_suite.json                # Auto-generated GX suite (rules)
│
│── gx_reports/                           # Great Expectations validation HTML docs
│
│── notebooks/
│   ├── eda.ipynb                         # Exploratory data analysis notebook
│   └── data_cleaning.ipynb               # Data cleaning & preprocessing notebook
│
│── scripts/
│   ├── create_expectations.py            # Define expectations/rules
│   ├── run_validation.py                 # Run checks + save summary
│   ├── build_charts.py                   # Generate matplotlib/seaborn plots
│   └── data/                             # Local outputs for scripts     
│       └── plots/
│           ├── overall_success_rate.png
│           ├── failures_by_column.png
│           ├── success_heatmap.png
│           └── latest_run_snapshot.png
│
│── governance/
│   └── collibra_glossary.md              # Mockup of business glossary
│
│── README.md                             # Case study writeup
│── requirements.txt                      # Dependencies


