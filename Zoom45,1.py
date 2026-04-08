import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset = pd.read_csv("Zooms/Data Science/iris.csv")
# print(dataset.head)
# print(dataset.info)

print(dataset["species"].unique())
dataset["species"] = dataset["species"].str.strip()

dataset["species"] = dataset["species"].replace({"setosa":0,"versicolor":1,"virginica":2})

# plt.subplot(221)
# plt.scatter(dataset["petal_length"], dataset["species"], s=10,c="green")
# plt.yticks(np.arange(1,4,1))
# plt.subplot(222)
# plt.scatter(dataset["petal_width"], dataset["species"], s=10, c="red")
# plt.yticks(np.arange(1,4,1))
# plt.show()

y = dataset["species"]
x = dataset.drop("species",axis=1)
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.head())

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))
