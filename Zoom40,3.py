# HW
"""
Create another column AgeGroup
Child if age < 12, Teen if age 12-18, Adult if age > 18
Count how many passengers are in each group
"""

import pandas as pd
import numpy as np

data = pd.read_csv("Zooms/Data Science/titanic.csv")

conditions=[
    (data["Age"]<12),
    ((data["Age"]>=12) & (data["Age"]<18)),
    (data["Age"]>=18)
]

choices = ["Child","Teen","Adult"]
data["AgeGroup"] = np.select(conditions,choices,default="Unknown")
print(data.head())

print(data["AgeGroup"].value_counts())