
"""
AI: decision making, texting processing, visual perception.
AI: allows computers to mimic human intelligence.
ML: improve at tasks with experience.
DL: use large datasets to mathematically mimic the human brain.

AI > ML > DL

Supervised learning: training algorithms using labelled data
Unsupervised learning: training algorithms with no labelled data
Reinforcement learning: algorithms take actions to maximise cumulative reward.


1. Import dataset (csv or api files)
2. Data preprocessing (any missing data?, clean data, remove duplicates)
3. Data visualisation (creating graphs,charts, etc)
4. Train Test Split (dividing the dataset into training and testing set)
-> Suppose 100 rows (use 70 for training and 30 for training - see if it's working)
5. Construct the model (put training data to train the model)
6. Tuning the model (getting the accuracy high)
7. Generating reports
8. Predict Results based on Model

"""
import pandas as pd
import numpy as np

dataset = pd.read_csv("Zooms/Data Science/createddata.csv")
x = dataset.iloc[:,:-1].values # Take all rows: Take all columns except last one
y = dataset.iloc[:,-1].values 

print(x)
print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(x[:,2:4])
x[:,2:4] = imputer.transform(x[:,2:4])
print(x)

#Encoding categorical data

# Encoding the independent varaible
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(), [0])],remainder="passthrough")
x = np.array(ct.fit_transform(x))
print(x)

# Encoding the dependent variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform
print(y)


