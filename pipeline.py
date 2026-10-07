import pandas as pd
from pathlib import Path

# ==============================
# 1. Project paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

# Change this filename if your raw dataset has a different name
DATA_FILE = BASE_DIR / "data" / "Amazon Sale Report.csv"

OUTPUT_DIR = BASE_DIR / "automation" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==============================
# 2. Load raw data
# ==============================

print("Loading dataset...")

df = pd.read_csv(DATA_FILE)

print(f"Dataset loaded successfully: {df.shape}")


# ==============================
# 3. Data cleaning
# ==============================

print("Cleaning data...")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Convert Amount to numeric if available
if "Amount" in df.columns:
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# Remove rows where important values are missing
if "Amount" in df.columns:
    df = df.dropna(subset=["Amount"])


# ==============================
# 4. KPI calculations
# ==============================

print("Calculating KPIs...")

total_orders = len(df)

total_sales = df["Amount"].sum() if "Amount" in df.columns else 0

average_order_value = (
    df["Amount"].mean()
    if "Amount" in df.columns
    else 0
)

if "Category" in df.columns:
    top_category = (
        df["Category"]
        .value_counts()
        .idxmax()
    )
else:
    top_category = "Not available"


# ==============================
# 5. Create KPI report
# ==============================

kpi_data = {
    "KPI": [
        "Total Orders",
        "Total Sales",
        "Average Order Value",
        "Top Category"
    ],
    "Value": [
        total_orders,
        round(total_sales, 2),
        round(average_order_value, 2),
        top_category
    ]
}

kpi_df = pd.DataFrame(kpi_data)


# ==============================
# 6. Save processed dataset
# ==============================

processed_file = OUTPUT_DIR / "processed_data.csv"

df.to_csv(processed_file, index=False)

print(f"Processed data saved to: {processed_file}")


# ==============================
# 7. Save KPI report to Excel
# ==============================

excel_file = OUTPUT_DIR / "KPI_Report.xlsx"

with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    kpi_df.to_excel(
        writer,
        sheet_name="KPI Summary",
        index=False
    )

    df.head(100).to_excel(
        writer,
        sheet_name="Sample Data",
        index=False
    )

print(f"KPI report saved to: {excel_file}")

print("\nAutomation pipeline completed successfully!")