import streamlit as st

st.header('Latest SIT proxy')

st.write("Latest ice conditions:")

#===================================
import sys
sys.path.append('./suboptions/')
import download
import pandas as pd
import plotly.express as px #if using plotly
import geopandas as gpd
import datetime
import calendar

#@st.cache_data
def get_date_lastchart():
    #Get date of last ice chart
    today = datetime.date.today()
    monday_date = today + datetime.timedelta(days=-today.weekday())
    weekday_no = datetime.datetime.today().weekday()  # Mo=0, Thursday=3
    if weekday_no>=3:  #If Thursday or later in the week
        date = monday_date
    else:
        date = monday_date - datetime.timedelta(weeks=1)
    date = f"{date.day:02}"+f"{date.month:02}"+str(date.year)
    return date, monday_date

@st.cache_data
def get_shpfile(date, location, monday_date):
    #set up the file path and read the shapefile data
    try:
        fp = './data/operational/'+date+'_CEXPR'+location+'_withsit.shp'
        data = gpd.read_file(fp)
    except:
        try:
            date = monday_date - datetime.timedelta(weeks=1)
            fp = './data/operational/'+date+'_CEXPR'+location+'_withsit.shp'
            data = gpd.read_file(fp)
        except:
            st.warning('Recent sea ice thickness product not yet available, please try again later', icon="⚠️")
            st.stop()
    return data

date, monday_date = get_date_lastchart()
shp_wa = get_shpfile(date, 'WA', monday_date)
shp_ea = get_shpfile(date, 'EA', monday_date)

shp_wa["geometry"] = (shp_wa.to_crs(shp_wa.estimate_utm_crs()).simplify(1000).to_crs(shp_wa.crs))
shp_ea["geometry"] = (shp_ea.to_crs(shp_ea.estimate_utm_crs()).simplify(1000).to_crs(shp_ea.crs))

#Create figure
fig = px.choropleth(shp_ea, 
                    geojson=shp_ea.geometry, 
                    locations=shp_ea.index, 
                    color="SIT",
                    width=1000,
                    height=1000,
                    color_continuous_scale="Spectral_r",
                    hover_data = ['SIT'])
fig2 = px.choropleth(shp_wa, 
                     geojson=shp_wa.geometry, 
                     locations=shp_wa.index, 
                     color="SIT",
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
            subunitwidth = 0.5),
        title_text=f'Sea ice thickness - {date[0:2]} {calendar.month_name[int(date[2:4])]} {str(date[4:8])}',
        margin={"r":0,"l":0,"t":30,"b":0},
        coloraxis_colorbar={'title':'SIT [m]'})
fig.update_geos(fitbounds="locations", visible=True,
                projection_type="stereographic",resolution=50,
                lataxis_showgrid=True, lonaxis_showgrid=True)

st.plotly_chart(fig)

# Add download button
merge = pd.concat([shp_wa, shp_ea])
download.add_downloadbutton_shp(date, merge)


# Add reference citation
st.markdown("""
<style>
.big-font {
    font-size:13px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">When using the data please cite:  \nGlissenaar, I. A., Landy, J. C., Babb, D. G., Dawson, G. J., and Howell, S. E. L.: A long-term proxy for sea ice thickness in the Canadian Arctic: 1996–2020, EGUsphere [preprint], https://doi.org/10.5194/egusphere-2023-269, 2023.</p>', unsafe_allow_html=True)

    