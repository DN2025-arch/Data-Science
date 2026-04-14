import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"C:\Users\flori\OneDrive\Desktop\Python\Visual Code\Zooms\Data Science\covid_data.csv")
print(data.head())

data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]
data.columns = ("State","Country","Last Update","Lat","Long","Confirmed","Recovered","Deaths","Active")

data["State"].fillna(value="",inplace=True)

top10_confirmed = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
fig1 = px.scatter(top10_confirmed, x=top10_confirmed.index, y="Confirmed",size="Confirmed",size_max=120,color=top10_confirmed.index,title="Top 10 Countries by Confirmed Cases")
fig1.write_html(r"C:\Users\flori\OneDrive\Desktop\Python\Visual Code\Zooms\Data Science\Fig1.html", auto_open=True)

fig2 = px.bar(top10_confirmed, x=top10_confirmed.index, y="Confirmed",color=top10_confirmed.index,title="Top 10 Countries by Confirmed Cases")
fig2.write_html(r"C:\Users\flori\OneDrive\Desktop\Python\Visual Code\Zooms\Data Science\Fig2.html", auto_open=True)

top10_recovered = pd.DataFrame(data.groupby("Recovered")["Recovered"].sum().nlargest(10).sort_values(ascending=False))
fig3 = px.bar(top10_recovered, x=top10_recovered.index, y="Recovered",color=top10_recovered.index,title="Top 10 Countries by Recovered Cases")
fig3.write_html(r"C:\Users\flori\OneDrive\Desktop\Python\Visual Code\Zooms\Data Science\Fig3.html", auto_open=True)

topStates_US = data["Country"]=="US"
topStates_US=data[topStates_US].nlargest(5,"Confirmed")
print(topStates_US)

topStates_JP = data["Country"]=="Japan"
topStates_JP=data[topStates_JP].nlargest(5,"Confirmed")
print(topStates_JP)

fig4 = go.Figure(data=[
    go.Bar(name="Confirmed Cases",x=topStates_US["Confirmed"], y=topStates_US["State"],orientation="h"),
    go.Bar(name="Confirmed Cases",x=topStates_JP["Confirmed"], y=topStates_JP["State"],orientation="h")
])

fig4.write_html(r"C:\Users\flori\OneDrive\Desktop\Python\Visual Code\Zooms\Data Science\Fig4.html", auto_open=True)
