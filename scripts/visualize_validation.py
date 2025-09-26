import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# ==============================
# 1. Load data
# ==============================
df = pd.read_csv("../data/walmart_validation_summary.csv")

# Ensure plots folder exists
os.makedirs("data/plots", exist_ok=True)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Fill success_rate if missing
df["success_rate"] = df.apply(
    lambda row: (1 - row["unexpected_count"] / row["total_count"]) * 100
    if pd.isna(row["success_rate"]) and row["total_count"] > 0
    else row["success_rate"],
    axis=1
)

# ==============================
# 2. Overall Success Rate Trend
# ==============================
plt.figure(figsize=(10, 5))
sns.lineplot(
    data=df.groupby("timestamp")["success_rate"].mean().reset_index(),
    x="timestamp", y="success_rate", marker="o"
)
plt.title("Validation Success Rate Over Time")
plt.ylabel("Success %")
plt.xlabel("Validation Run")
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.savefig("data/plots/overall_success_rate.png")
plt.close()

# ==============================
# 3. Failures by Column
# ==============================
plt.figure(figsize=(10, 5))
failures_by_col = df.groupby("column")["unexpected_count"].sum().reset_index()
sns.barplot(data=failures_by_col, x="column", y="unexpected_count", palette="Reds_r")
plt.title("Total Failures by Column")
plt.ylabel("Unexpected Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/plots/failures_by_column.png")
plt.close()

# ==============================
# 4. Expectation Success Rate Heatmap
# ==============================
pivot = df.pivot_table(
    index="column", columns="expectation_type", values="success_rate", aggfunc="mean"
)
plt.figure(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="RdYlGn", cbar_kws={'label': 'Success %'})
plt.title("Expectation Success Rates per Column")
plt.tight_layout()
plt.savefig("data/plots/success_heatmap.png")
plt.close()

# ==============================
# 5. Latest Run Snapshot
# ==============================
latest_run = df[df["timestamp"] == df["timestamp"].max()]
plt.figure(figsize=(10, 5))
sns.barplot(data=latest_run, x="column", y="success_rate", hue="expectation_type", palette="viridis")
plt.title(f"Validation Snapshot ({latest_run['timestamp'].iloc[0].strftime('%Y-%m-%d %H:%M')})")
plt.ylabel("Success %")
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("data/plots/latest_run_snapshot.png")
plt.close()

print("✅ Validation charts saved in data/plots/")
