# Data Dictionary

## Database: bluestock_mf.db

This database stores mutual fund master information and historical NAV data for analysis.

---

# Table: dim_fund

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company name |
| scheme_name | TEXT | Name of mutual fund scheme |
| category | TEXT | Fund category |
| sub_category | TEXT | Detailed category |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Fund launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio percentage |
| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | REAL | Minimum SIP investment amount |
| min_lumpsum_amount | REAL | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk classification |
| sebi_category_code | TEXT | SEBI category code |

Primary Key:
- amfi_code

---

# Table: fact_nav

| Column Name | Data Type | Description |
|------------|------------|------------|
| nav_id | INTEGER | Unique NAV record identifier |
| amfi_code | INTEGER | AMFI code of the scheme |
| nav_date | DATE | Date of NAV |
| nav | REAL | Net Asset Value |

Primary Key:
- nav_id

Foreign Key:
- amfi_code → dim_fund(amfi_code)

---

# Data Sources

1. fund_master.csv
   - Contains fund metadata and scheme information.

2. nav_history.csv
   - Contains historical NAV records for mutual fund schemes.

---

# Cleaning Performed

## fund_master.csv

- Removed duplicate AMFI codes.
- Converted launch_date to datetime format.
- Standardized missing values.

## nav_history.csv

- Converted date column to datetime.
- Sorted data by AMFI code and date.
- Forward-filled missing NAV values.
- Removed invalid NAV values (NAV <= 0).
- Removed duplicate records.

---

# Purpose

The database is designed for:

- Mutual Fund Analytics
- NAV Trend Analysis
- Expense Ratio Comparison
- Fund House Analysis
- Historical Performance Tracking
- SQL-Based Reporting