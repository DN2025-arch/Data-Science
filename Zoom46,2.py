import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"Zooms\Data Science\covid_data.csv")
data["Combined"] = data["Deaths"] + data["Confirmed"] + data["Recovered"]

topStates_US_deaths= data["Country_Region"]=="US"
topStates_US_deaths= data[topStates_US_deaths].nlargest(5,"Deaths")
topStates_US_combined= data["Country_Region"]=="US"
topStates_US_combined= data[topStates_US_combined].nlargest(5,"Combined")
print(topStates_US_deaths)
print(topStates_US_combined)

topStates_IN_deaths = data["Country_Region"]=="India"
topStates_IN_deaths=data[topStates_IN_deaths].nlargest(5,"Deaths")
topStates_IN_combined= data["Country_Region"]=="India"
topStates_IN_combined= data[topStates_IN_combined].nlargest(5,"Combined")
print(topStates_IN_deaths)
print(topStates_IN_combined)

fig1 = px.bar(topStates_US_deaths,x=topStates_US_deaths["Province_State"],y="Deaths")
fig1.write_html("Zooms\Data Science\Fig2-1.html",auto_open=True)

fig2 = px.bar(topStates_IN_deaths,x=topStates_IN_deaths["Province_State"],y="Deaths")
fig2.write_html("Zooms\Data Science\Fig2-2.html",auto_open=True)
