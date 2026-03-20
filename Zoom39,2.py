# HW Here:
"""HW: Load Titanic Dataset, Answer Questions:

How many passengers were above 60?
How many females travelled in 1st class?
What is the Average fare for 3rd class passengers
How many children (Age < 12) survived?
"""

import pandas as pd

data = pd.read_csv("Zooms/Data Science/titanic.csv")
#print(data.head())

passengers_abv60 = data[data["Age"]>60]
female1stclass = data[(data["Sex"]=="female") & (data["Pclass"]==1)]
thirdclass = data[data["Pclass"]==3]
thirdclassfares = thirdclass["Fare"]
avgfare3rdclass = thirdclassfares.mean()
childrensurvived = data[(data["Survived"]==1) & (data["Age"]<12)]

print(passengers_abv60.head())
print(female1stclass.head())
print(avgfare3rdclass)
print(childrensurvived.head())