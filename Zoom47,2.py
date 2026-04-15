import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"Zooms\Data Science\adult.csv")

data["Capital-Gain"] = data["Capital-Gain"].fillna(data["Capital-Gain"].mean())
data["Capital-Loss"] = data["Capital-Loss"].fillna(data["Capital-Loss"].mean())

data["Salary"] = data["Salary"].replace({"<=50K":0,">50K":1})
data["Sex"] = data["Sex"].replace({"Male":0,"Female":1})

fig1 = px.bar(data, x=data["Job"], y="Final-Wage")
fig1.write_html("Zooms\Data Science\Fig4-1.html",auto_open=True)

# HW: Further analysis, for example: How does gender correspond to salary.
