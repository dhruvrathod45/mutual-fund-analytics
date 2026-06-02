import requests
import pandas as pd
import os

schemes = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

current_dir = os.path.dirname(os.path.abspath(__file__))
save_folder = os.path.join(current_dir, "..", "data", "raw")

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        os.path.join(save_folder, f"{name}.csv"),
        index=False
    )

    print(f"{name} saved")