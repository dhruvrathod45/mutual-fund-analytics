import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

fund_master_path = os.path.join(
    current_dir,
    "..",
    "data",
    "raw",
    "fund_master.csv"
)

nav_history_path = os.path.join(
    current_dir,
    "..",
    "data",
    "raw",
    "nav_history.csv"
)

fund_master = pd.read_csv(fund_master_path)
nav_history = pd.read_csv(nav_history_path)

missing_codes = set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])

print("Missing AMFI Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("All AMFI codes validated successfully.")
else:
    print(missing_codes)