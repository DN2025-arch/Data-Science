import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

time_series = pd.read_csv(r"Zooms\Data Science\WHO-COVID-19-global-data.csv", encoding="ISO-8859-1")
time_series.columns = ("Date_Reported","Country_Code","Country","WHO_Region","New_Cases",
                       "Cumulative_Cases","New_Deaths","Cumulative_Deaths")
time_series["Date_Reported"] = pd.to_datetime(time_series["Date_Reported"])

time_series_dates = time_series.groupby("Date_Reported").sum()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=time_series_dates.index,y=time_series_dates["Cumulative_Cases"],fill="tonexty",line_color="blue"))
fig1.update_layout(title="Cumulative Cases Worldwide")
fig1.show()
#fig1.write_html("Zooms\Data Science\Fig3-1.html",auto_open=True)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=time_series_dates.index,y=time_series_dates["Cumulative_Deaths"],fill="tonexty",line_color="red"))
fig2.update_layout(title="Cumulative Deaths Worldwide")
fig2.show()
#fig2.write_html("Zooms\Data Science\Fig3-2.html",auto_open=True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=time_series_dates.index,y=time_series_dates["New_Cases"],fill="tonexty",line_color="gold"))
fig3.update_layout(title="New Cases Worldwide")
fig3.show()
#fig3.write_html("Zooms\Data Science\Fig3-1.html",auto_open=True)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=time_series_dates.index,y=time_series_dates["New_Deaths"],fill="tonexty",line_color="hotpink"))
fig4.update_layout(title="New Deaths Worldwide")
fig4.show()
#fig4.write_html("Zooms\Data Science\Fig3-2.html",auto_open=True)