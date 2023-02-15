import streamlit as st

st.header('Operational SIT proxy')
st.write("Latest ice conditions:")

#===================================

import pandas as pd
import matplotlib.pyplot as plt #if using matplotlib
import plotly.express as px #if using plotly
import geopandas as gpd
import datetime
import calendar

#Get date of last ice chart
today = datetime.date.today()
monday_date = today + datetime.timedelta(days=-today.weekday())
weekday_no = datetime.datetime.today().weekday()  # Mo=0, Thursday=3
if weekday_no>=3:  #If Thursday or later in the week
    date = monday_date
else:
    date = monday_date - datetime.timedelta(weeks=1)
date = f"{date.day:02}"+f"{date.month:02}"+str(date.year)

#set up the file path and read the shapefile data
#Western Arctic
fp = './data/operational/'+date+'_CEXPREA_withsit.shp'
data = gpd.read_file(fp)
data = data.to_crs(epsg=4326)


#set up the file path and read the shapefile data
#Eastern Arctic
fp = './data/operational/'+date+'_CEXPRWA_withsit.shp'
data2 = gpd.read_file(fp)
data2 = data2.to_crs(epsg=4326)


#merged = pd.concat([data, data2])


#Create figure
fig = px.choropleth(data, geojson=data.geometry, 
                    locations=data.index, color="sit",
                    width=1000,
                    height=500,
                   color_continuous_scale="Spectral_r")
fig2 = px.choropleth(data2, geojson=data2.geometry, 
                    locations=data2.index, color="sit",
                    width=1000, height=500,
                   color_continuous_scale="Spectral_r")
fig.add_trace(fig2.data[0])
fig.update_geos(fitbounds="locations", visible=True)
fig.update_geos(projection_type="orthographic",resolution=50)
fig.update_layout(
    title_text=f'SIT {date[0:2]} {calendar.month_name[int(date[2:4])]} {str(date[4:8])}'
)
#fig.update(layout = dict(title=dict(x=0.5)))
fig.update_layout(
    margin={"r":0,"t":30,"l":10,"b":10},
    coloraxis_colorbar={
        'title':'SIT [m]'})

st.plotly_chart(fig, use_container_width=True)



