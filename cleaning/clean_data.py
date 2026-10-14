"""
Task 1 - Global Superstore Data Cleaning

Place the raw .xlsm file in:
data/raw/global_superstore_raw.xlsm

Run:
python cleaning/clean_data.py

Output:
data/cleaned/global_superstore_cleaned.csv
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "global_superstore_raw.xls"
OUTPUT_FILE = PROJECT_ROOT / "data" / "cleaned" / "global_superstore_cleaned.csv"
EXCEL_OUTPUT_FILE = PROJECT_ROOT / "data" / "cleaned" / "global_superstore_cleaned.xlsx"

def main():
    if not RAW_FILE.exists():
        print("\nERROR: Raw dataset not found.")
        print(f"Put your file here:\n{RAW_FILE}\n")
        return

    print("=" * 70)
    print("GLOBAL SUPERSTORE - TASK 1 DATA CLEANING")
    print("=" * 70)

    # Read the first sheet from the Excel macro-enabled workbook.
    df = pd.read_excel(RAW_FILE, sheet_name=0, engine="xlrd")

    original_rows, original_cols = df.shape
    print(f"\nOriginal shape: {df.shape}")

    # Remove completely empty rows and columns.
    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")

    # Standardize column labels.
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    # Trim whitespace in text columns.
    text_columns = df.select_dtypes(include=["object", "string"]).columns
    for col in text_columns:
        df[col] = df[col].astype("string").str.strip()

    # Convert common date columns.
    date_columns = [
        col for col in ["Order Date", "Ship Date"]
        if col in df.columns
    ]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Convert common numeric columns.
    numeric_columns = [
        "Row ID", "Sales", "Quantity", "Discount",
        "Profit", "Shipping Cost"
    ]
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Treat empty strings as missing values.
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Remove exact duplicate rows.
    duplicate_count = int(df.duplicated().sum())
    if duplicate_count:
        df = df.drop_duplicates()

    # Save cleaned dataset.
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Use ISO-style date text for easy Power BI/CSV compatibility.
    export_df = df.copy()
    for col in date_columns:
        export_df[col] = export_df[col].dt.strftime("%Y-%m-%d")

    export_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    export_df.to_excel(EXCEL_OUTPUT_FILE, index=False, engine="openpyxl")

    # Cleaning summary.
    print("\n" + "-" * 70)
    print("CLEANING SUMMARY")
    print("-" * 70)
    print(f"Original rows:              {original_rows}")
    print(f"Original columns:           {original_cols}")
    print(f"Final rows:                 {len(df)}")
    print(f"Final columns:              {len(df.columns)}")
    print(f"Exact duplicate rows found: {duplicate_count}")
    print(f"Missing values remaining:    {int(df.isna().sum().sum())}")

    print("\nMissing values by column:")
    missing = df.isna().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print("None")
    else:
        print(missing.to_string())

    print("\nData types:")
    print(df.dtypes.to_string())

    print("\nCleaned file created:")
    print(OUTPUT_FILE)
    print("\nTASK 1 COMPLETE.")

if __name__ == "__main__":
    main()
