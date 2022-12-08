import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import cartopy.crs as ccrs
import numpy as np
import xarray as xr
import pandas as pd
from scipy import stats
import calendar
import cartopy.feature as cfeature
land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m')

st.header('Opertational SIT proxy')
st.write("Work in progress: this page will display this week's ice thickness soon...")










#m = 4
#year = 2000

#direc = 'C:/Users/zq19140/OneDrive - University of Bristol/Documents/Projects/icecharts_thickness/data/processed/predicted_sit_edit/'
#sit = xr.open_dataset(direc+'predic_sit_19932020_'+f"{m:02}"+'.nc')
#y = np.where(sit.year==year)[0][0]

#d = {'lat': sit.lat.values, 
#     'lon': sit.lon.values,
#     'sit': sit.sit_mean[y,:].values}
#df = pd.DataFrame(data=d)
#df = df.dropna()
#    
#def colorsscatter(df):
#    cmap = matplotlib.cm.get_cmap('Spectral_r')
#    color = cmap(df.sit.values/3)*255
#    return(color[:,0],color[:,1],color[:,2])#

#df['r'],df['g'],df['b'] = colorsscatter(df)

#import pydeck as pdk

#st.pydeck_chart(pdk.Deck(
#    map_style=None,
#    initial_view_state=pdk.ViewState(
#        latitude=76,
#        longitude=-116,
#        zoom=1.5,
#    ),
#    layers=[        
#        pdk.Layer(
#           'ScatterplotLayer',
#            data=df,
#            get_position='[lon, lat]',                
#            get_fill_color=['r', 'g', 'b'],
#            get_line_color=[0, 0, 0],
#            get_radius=30000,
#            opacity=0.8
#        ),
#    ],
#))


