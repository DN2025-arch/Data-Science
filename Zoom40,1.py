import pandas as pd
import numpy as np

data = pd.read_csv("Zooms/Data Science/titanic.csv")

# Get the particular column out of a condition
adult_names = data.loc[data["Age"]>18,"Name"]
print(adult_names.head())

# Slicing - same as numpy 2D slicing
# First Index: Rows, Second Index: Columns, same syntax as range function
print(data.iloc[9:25,2:5])
# Change the value in the dataset
data.iloc[0:3, 2] = "Pulkit Chawla"
print(data["Name"])

# Save the data to a local to verify changes
data.to_csv("Zooms/Data Science/titanic2.csv")

# Creating a new column in the dataFrame
'''data["Taxed Fare"] = data["Fare"] + 2'''
data["Taxed Fare"] = data["Fare"] * data["Pclass"]

# Renaming the column names
data_renamed = data.rename(
    columns={
        "Pclass":"Passenger Class",
        "Siblings/Spouses Aboard":"Sibsp",
    }
)

print(data_renamed.info())

# Performing mathematical operation on multiple columns together
print(data["Age"].mean())
print(data[["Age","Fare"]].mean()) # Mean of age then mean of fare
print(data.agg({ # agg(revating) is for doing multiple math operations at once
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max", "median"]
}))

# Group by data categorically
print(data[["Sex","Age"]].groupby("Sex").mean()) # All "female" and "male" values are separated and takes mean of each.
print(data.groupby("Sex")["Age"].mean())

# Task - Get main ticket price for each sex and cabin class combination
print(data.groupby(["Sex","Pclass"])["Fare"].mean()) # Separates Sex and Pclass values

# Get the count of rows in each category
print(data["Pclass"].value_counts())
print(data.groupby("Pclass")["Pclass"].count())

# Sorting the data
data.sort_values(by="Age")
print(data[["Name","Age"]].head())
data.sort_values(by=["Pclass","Age"],ascending=False)

# Operations on Text Data
data["NameLowercase"] = data["Name"].str.lower()
data["NameUppercase"] = data["Name"].str.upper()
data["Surname"] = data["Name"].str.split(" ").str.get(2) # get(2) will get the third splitted value
print(data["Surname"])

# Replacing values in the sex column (male -> M, female -> F)
data["Sex_short"] = data["Sex"].replace({"male":"M","female":"F"})
print(data.head())