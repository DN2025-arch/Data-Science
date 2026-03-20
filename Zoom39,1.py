import numpy as np # Math
import pandas as pd # Data

# USI Machine Learning website for data.
# csv files separate data using commas.

# Creating Data:
student_data = {
    "name":     ["Alice", "Bob", "John", "Mary", "John", "Benny", "Henry", "Polly"],
    "age":      [10,12,14,9,11,12,13,14],
    "fav_color":["White","Green","Orange","Yellow","Gray","Brown","Black","Pink",]
}
print(student_data)
# Convert raw data into dataframe (Matrix Form)
dataset = pd.DataFrame(student_data) # Turn Dictionary into Dataframe
print(dataset)

print(dataset.head()) # Shows only the first five entries.
print(dataset.shape)  # Output: (8,3) = (Rows, Columns)


print(dataset["name"]) # Focus on any one column from dataset
print(dataset["age"].max()) # Shows largest number
print(dataset["age"].min()) # Shows smallest number

print(dataset.info()) # Get Summary of the data
# non-null: none of the entries are nil.
print(dataset.describe()) # Gives numerical operations of numerical columns.



# CSV: Comma Separated Value (File)
data = pd.read_csv("Zooms/Data Science/titanic.csv")
print(data.head()) # Check if properly read
print(data.info())
print(data.describe())

print(data.dtypes) # Shows the datatypes for each column

# Select 2-3 columns together: (For CSVs)
name_and_age = data[["Name","Age"]]
print(name_and_age.head())

# Filtering out rows
above35 = data[data["Age"]>35]
print(above35["Age"].head())

# Combining Conditions Together
class2and3 = data[data["Pclass"].isin([2,3])]
#print(class2and3["Name"].head())
print(class2and3[["Name", "Pclass"]].head())

# Alternative Method
class2and3 = data[(data["Pclass"]==2) | (data["Pclass"]==3)] # Note: "|" is OR, and & is for AND

# Task - Get the mean fare of people in Pclass 1 wrt Sex-Male.

task1data = data[(data["Pclass"]==1) & (data["Sex"]=="male")]
task1data_fares = task1data["Fare"]
print(task1data_fares.head())
print(task1data_fares.mean()) # Find Mean
