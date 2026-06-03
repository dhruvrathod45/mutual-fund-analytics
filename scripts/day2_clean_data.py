import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# FUND MASTER
funds = pd.read_csv("data/raw/fund_master.csv")

funds["launch_date"] = pd.to_datetime(
    funds["launch_date"],
    errors="coerce"
)

funds = funds.drop_duplicates(
    subset=["amfi_code"]
)

funds.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

# NAV HISTORY
nav = pd.read_csv("data/raw/nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav[nav["nav"] > 0]

nav = nav.drop_duplicates()

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Cleaning completed")