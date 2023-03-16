import calendar

import numpy as np
import plotly.graph_objects as go
import streamlit as st
import xarray as xr

    
    
def sitfig(m,year):
    direc = './data/'
    sit = xr.open_dataset(direc+'proxy_sit_canadianarctic_19962020_'+f"{m:02}"+'.nc')
    y = np.where(sit.year==year)[0][0]
    p = sit.sit_mean[y,:].values
    
    #Create figure
    fig = go.Figure(data=go.Scattergeo(
        lon = sit['lon'][~np.isnan(p)],
        lat = sit['lat'][~np.isnan(p)],
        text = p[~np.isnan(p)],
        mode = 'markers',
        marker_color = p[~np.isnan(p)],
        marker = dict(
            colorscale = 'Spectral_r',
            cmin = 0,
            cmax = 3,
            colorbar = dict(
                titleside = "right",),
            colorbar_title = 'm'
            )
        ))
    fig.update_layout(
        geo = dict(
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5),
        title_text=f' ',
        width=1000,
        height=1000,
        margin={"r":0,"l":0,"t":0,"b":0},
        coloraxis_colorbar={'title':'SIT [m]'})
    fig.update_geos(fitbounds="locations", visible=True,
                    projection_type="stereographic",resolution=50,
                    lataxis_showgrid=True, lonaxis_showgrid=True)
    fig.update_traces(marker=dict(size=8))

    st.plotly_chart(fig, use_container_width=True)
    
    
    