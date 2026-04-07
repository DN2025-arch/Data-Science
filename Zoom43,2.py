import pandas as pd
import numpy as np
import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "titanic3.csv")
dataset = pd.read_csv(file_path)

dataset["Age"] = dataset["Age"].fillna(dataset["Age"].mean())

dataset["Embarked"] = dataset["Embarked"].fillna(dataset["Embarked"].mode()[0])

dataset = pd.get_dummies(dataset, columns=["Sex","Embarked"], drop_first=True)

y = dataset["Survived"].values

dropping_columns = ["Survived","PassengerId","Name","Ticket","Cabin"]
dropping_columns = [col for col in dropping_columns if col in dataset.columns]

x = dataset.drop(columns=dropping_columns).values
print(x[0])
print(y[:5])
