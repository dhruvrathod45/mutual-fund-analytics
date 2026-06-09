import pandas as pd

df = pd.read_csv("../reports/fund_scorecard.csv")

print("\nTop Recommended Funds\n")

top = df.sort_values(
    "sharpe",
    ascending=False
).head(5)

print(
    top[
        [
            "amfi_code",
            "sharpe",
            "score"
        ]
    ]
)