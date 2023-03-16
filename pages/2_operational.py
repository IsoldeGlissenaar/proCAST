import streamlit as st

st.header('Operational SIT proxy')
st.write("Latest ice conditions:")

#===================================
import sys
sys.path.append('./suboptions/')
import download
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
try:
    fp = './data/operational/'+date+'_CEXPREA_withsit.shp'
    data = gpd.read_file(fp)
except:
    try:
        date = monday_date - datetime.timedelta(weeks=1)
        fp = './data/operational/'+date+'_CEXPREA_withsit.shp'
        data = gpd.read_file(fp)
    except:
        st.warning('Recent sea ice thickness product not yet available, please try again later', icon="⚠️")
        st.stop()

#set up the file path and read the shapefile data
#Eastern Arctic
try:
    fp = './data/operational/'+date+'_CEXPRWA_withsit.shp'
    data2 = gpd.read_file(fp)
except:
    try:
        date = monday_date - datetime.timedelta(weeks=1)
        fp = './data/operational/'+date+'_CEXPRWA_withsit.shp'
        data2 = gpd.read_file(fp)    
    except:
        st.warning('Recent sea ice thickness product not yet available, please try again later', icon="⚠️")
        st.stop()

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



st.markdown("""
<style>
.big-font {
    font-size:13px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">When using the data please cite:  \nGlissenaar, I. A., Landy, J. C., Babb, D. G., Dawson, G. J., and Howell, S. E. L.: A long-term proxy for sea ice thickness in the Canadian Arctic: 1996–2020, EGUsphere [preprint], https://doi.org/10.5194/egusphere-2023-269, 2023.</p>', unsafe_allow_html=True)

    