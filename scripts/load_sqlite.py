import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

funds = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

funds.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Database created")