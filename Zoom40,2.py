import pandas as pd
import numpy as np

# price per person: fare / (sibling count + 1)
data = pd.read_csv("Zooms/Data Science/titanic.csv")

data["Price Per Person"] = data["Fare"] / (data["Siblings/Spouses Aboard"] + 1)

print(data["Price Per Person"].head())


# extract mr/ms, use groupby to find avg mean of age

data["Surnames"] = data["Name"].str.split(" ").str.get(0)
print(data.groupby("Surnames")["Age"].mean())

# sort data by fare price - descending order, take top 10 rows, value_counts on sex column - how many male/female?

data_a = data.sort_values(by="Fare",ascending=False)
data_b = data_a.iloc[0:10]
print(data_b["Sex"].value_counts())

