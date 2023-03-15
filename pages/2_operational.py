import sys
sys.path.append('./suboptions/')

import calendar
import datetime

import download
import geopandas as gpd
import pandas as pd
import plotly.express as px  # if using plotly
import streamlit as st


st.header('Operational SIT proxy')
st.write("Latest ice conditions:")

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


#set up the file path and read the shapefile data
#Eastern Arctic
fp = './data/operational/'+date+'_CEXPRWA_withsit.shp'
data2 = gpd.read_file(fp)

#Create figure
fig = px.choropleth(data, geojson=data.geometry,
                    locations=data.index, color="SIT",
                    width=1000,
                    height=500,
                    color_continuous_scale="Spectral_r",
                    hover_data = ['SIT'])
fig2 = px.choropleth(data2, geojson=data2.geometry,
                    locations=data2.index, color="SIT",
                    width=1000, height=500,
                    color_continuous_scale="Spectral_r",
                    hover_data=["SIT"])
fig.add_trace(fig2.data[0])
fig.update_layout(
        geo = dict(
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
        title_text=f'SIT {date[0:2]} {calendar.month_name[int(date[2:4])]} {str(date[4:8])}',
        margin={"r":0,"t":30,"l":10,"b":10},
        coloraxis_colorbar={'title':'SIT [m]'}
    )
fig.update_geos(fitbounds="locations", visible=True,
                projection_type="orthographic",resolution=50)

st.plotly_chart(fig)

merge = pd.concat([data, data2])
download.add_downloadbutton_shp(date, merge)
