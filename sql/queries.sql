-- 1. Total number of funds
SELECT COUNT(*) AS total_funds
FROM dim_fund;

-- 2. Funds by category
SELECT category, COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category
ORDER BY fund_count DESC;

-- 3. Funds by fund house
SELECT fund_house, COUNT(*) AS total_funds
FROM dim_fund
GROUP BY fund_house
ORDER BY total_funds DESC;

-- 4. Average expense ratio by category
SELECT category,
       ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM dim_fund
GROUP BY category;

-- 5. Top 5 highest expense ratio funds
SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 6. Top 5 lowest expense ratio funds
SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
ORDER BY expense_ratio_pct ASC
LIMIT 5;

-- 7. Average NAV for each fund
SELECT amfi_code,
       ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- 8. Highest NAV recorded for each fund
SELECT amfi_code,
       MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC;

-- 9. Lowest NAV recorded for each fund
SELECT amfi_code,
       MIN(nav) AS lowest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY lowest_nav ASC;

-- 10. Year-wise average NAV
SELECT strftime('%Y', nav_date) AS year,
       ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY year
ORDER BY year;