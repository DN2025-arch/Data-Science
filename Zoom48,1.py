import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"Zooms\Data Science\student+performance\student\student-mat.csv",sep=";")


data["school"] = data["school"].map({"GP":0,"MS":1})
data["sex"] = data["sex"].map({"M":0,"F":1})
data["address"] = data["address"].map({"U":0,"R":1,})
data["famsize"] = data["famsize"].map({"GT3":0,"LE3":1,})
data["Pstatus"] = data["Pstatus"].map({"A":0,"T":1})
data["guardian"] = data["guardian"].map({"father":0,"mother":1,"other":2})
data["schoolsup"] = data["schoolsup"].map({"yes":0,"no":1})
data["famsup"] = data["famsup"].map({"yes":0,"no":1})
data["paid"] = data["schoolsup"].map({"yes":0,"no":1})
data["activities"] = data["activities"].map({"yes":0,"no":1})
data["nursery"] = data["schoolsup"].map({"yes":0,"no":1})
data["higher"] = data["higher"].map({"yes":0,"no":1})
data["internet"] = data["internet"].map({"yes":0,"no":1})
data["romantic"] = data["romantic"].map({"yes":0,"no":1})

data["outcome"] = (data["G3"]>=10).astype(int)
print(data["outcome"].head())

study_impact = data.groupby("studytime")["G3"].mean()
family_impact = data.groupby("famsup")["G3"].mean()
print(study_impact)

fig1 = px.bar(data,x=data["studytime"],y="G3")
fig1.write_html("Zooms\Data Science\Fig6-1.html",auto_open=True)
fig2 = px.bar(data,x=data["famsup"],y="G3")
fig2.write_html("Zooms\Data Science\Fig6-2.html",auto_open=True)

internet_impact = data.groupby("internet")["G3"].mean()
print(internet_impact)

fig3 = px.bar(data, x=data["internet"], y="G3")
fig3.write_html("Zooms\Data Science\Fig6-3.html",auto_open=True)