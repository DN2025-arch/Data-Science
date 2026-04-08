import pandas as pd
import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "coviddata.csv")
dataset = pd.read_csv(file_path)

dataset["Confirmed"] = dataset["Confirmed"].fillna(dataset["Confirmed"].mean())
dataset["Recovered"] = dataset["Recovered"].fillna(dataset["Recovered"].mean())
dataset["Deaths"]    = dataset["Deaths"].fillna(dataset["Deaths"].mean())

y = dataset["Deaths"]

x = dataset.drop(columns=["Country","Deaths"]).values

print(x[0])
print(y[0])
