import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(current_dir, "..", "data", "raw")

files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

for file in files:

    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(os.path.join(raw_path, file))

    print("Shape:")
    print(df.shape)

    print("Data Types:")
    print(df.dtypes)

    print("Head:")
    print(df.head())