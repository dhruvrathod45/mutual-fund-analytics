import requests
import pandas as pd
import os

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["data"])

current_dir = os.path.dirname(os.path.abspath(__file__))

save_path = os.path.join(
    current_dir,
    "..",
    "data",
    "raw",
    "hdfc_top100.csv"
)

df.to_csv(save_path, index=False)

print(df.head())