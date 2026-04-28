import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"Zooms\Data Science\heart+disease\processed.switzerland.csv")

fig1 = px.bar(data,x=data["age"],y="num")
fig1.write_html("Zooms\Data Science\Fig7-1.html",auto_open=True)

fig2 = px.bar(data,x=data["chol"],y="num")
fig2.write_html("Zooms\Data Science\Fig7-2.html",auto_open=True)

fig1 = px.bar(data,x=data["sex"],y="num")
fig1.write_html("Zooms\Data Science\Fig7-3.html",auto_open=True)
