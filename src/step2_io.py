
import pandas as pd
from src.dataset import make_df

df = make_df()

df.to_csv("data/data.csv", index=False)
df.to_excel("data/data.xlsx", index=False)
df.to_json("data/data.json", orient="records")

print(pd.read_csv("data/data.csv").shape)
print(pd.read_excel("data/data.xlsx").shape)
print(pd.read_json("data/data.json").shape)
print(open("data/data.json").read()[:60])
