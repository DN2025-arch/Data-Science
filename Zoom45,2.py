import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset = pd.read_csv("Zooms/Data Science/iris.csv")
print(dataset.head)
print(dataset.info)

dataset["species"] = dataset["species"].str.strip()
dataset["species"] = dataset["species"].replace({"setosa":0,"versicolor":1,"virginica":2})

y = dataset["species"]
x = dataset.drop("species",axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))

# Drop Sepal Length

x = dataset.drop(columns=["species","sepal_length"]).values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))

# Drop Sepal Width

x = dataset.drop(columns=["species","sepal_width"]).values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))

# Drop Petal Length

x = dataset.drop(columns=["species","petal_length"]).values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))

# Drop Petal Width

x = dataset.drop(columns=["species","petal_width"]).values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))