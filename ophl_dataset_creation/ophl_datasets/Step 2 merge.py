import pandas as pd
import glob
import os

csv_list = glob.glob("./*.csv")

df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
df.to_csv("Merged.csv")
print(f"{len(csv_list)} files successfully merged!!")
