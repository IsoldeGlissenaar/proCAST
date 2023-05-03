
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import shapefile as shp  # Requires the pyshp package
import streamlit as st
import xarray as xr
from scipy import stats
import geopandas as gpd
from shapely.geometry import Point, shape



def sittrendfig(m,year_1,year_2):
    direc = './data/'
    sit = xr.open_dataset(direc+'proxy_sit_canadianarctic_19962020_'+f"{m:02}"+'.nc')
    if (m==12)&(year_1==1996):
        year_1 = 1997
    elif m<5:
        sit = sit.drop(1997, dim='year')

    y1 = np.where(sit.year==year_1)[0][0]
    y2 = np.where(sit.year==year_2)[0][0]

    p_value = np.zeros(sit.dims['n'])
    trend_sit = np.zeros(sit.dims['n'])
    for i in range(sit.dims['n']):
        x=sit.year[y1:y2+1]
        y=sit.sit_mean_corr[y1:y2+1,i]

        trend_sit[i], intercept, r_value, p_value[i], std_err = stats.linregress(x, y)


    sit['trend'] = (['n'], trend_sit*100)
    sit['text'] = (['n'], (np.round(trend_sit*100,1)).astype(str))

    
    @st.cache_data
    def get_shpfile():
        #set up the file path and read the shapefile data
        fp = './data/shape_regions/v200_CISIRR_Regions_4326_merge.shp'
        data = gpd.read_file(fp)
        return data
    
    shp = get_shpfile()
    options = ['cwa04_00', 'tew02_00','cwa01_00','cea12_00']
    shp = shp[shp['SHORT_NAME'].isin(options)]
    shp["geometry"] = (shp.to_crs(shp.estimate_utm_crs()).simplify(1000).to_crs(shp.crs))

    #Create figure
    fig = go.Figure(data=go.Scattergeo(
        lon = sit['lon'][~np.isnan(trend_sit)],
        lat = sit['lat'][~np.isnan(trend_sit)],
        text = sit['text'][~np.isnan(trend_sit)],
        mode = 'markers',
        marker_color = sit['trend'][~np.isnan(trend_sit)],
        marker = dict(
            colorscale = 'RdBu',
            cmin = -5,
            cmax = 5,
            colorbar = dict(
                titleside = "right",
                ),
            colorbar_title = 'cm/yr'
            )
        ))
    fig.update_traces(marker=dict(size=9))
    
  #  fig2 = px.choropleth(shp, 
  #                   geojson=shp.geometry, 
  #                   locations=shp.index)    
  #  fig.add_trace(fig2.data[0])    
    
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

    st.plotly_chart(fig, use_container_width=True)



def timeline(m, year_1, year_2, name):
    if name=='Beaufort Sea':
        region = 'cwa01_00'
    elif name=='Arctic Ocean Periphery':
        region = 'tew02_00'
    elif name=='Parry Channel':
        region = 'cwa04_00'
    elif name=='Baffin Bay':
        region = 'cea12_00'

    direc = './data/'
    sit = xr.open_dataset(direc+'proxy_sit_canadianarctic_19962020_'+f"{m:02}"+'.nc')
    if (m==12)&(year_1==1996):
        year_1 = 1997
    elif m<5:
        sit = sit.drop(1997, dim='year')

    y1 = np.where(sit.year==year_1)[0][0]
    y2 = np.where(sit.year==year_2)[0][0]

    # Check in which CISIRR Region the grid cells are
    idx = []
    shp1 = shp.Reader('./data/shape_regions/v200_CISIRR_Regions_4326_merge.shp') #open the shapefile
    all_shapes = shp1.shapes() # get all the polygons
    all_records = shp1.records()
    len_f = sit.dims['n']
    location = []; p=0
    for i in range(len_f):
        pt = (sit.lon.values[i], sit.lat.values[i])
        for k in range (len(all_shapes)):
            boundary = all_shapes[k]
            if Point(pt).within(shape(boundary)):
                location.append(all_records[k][3])
                p=1
        if p==0:
            location.append(' ')
        p=0
    sit['location'] = (['n'], np.array(location))

    if name=='Full area':
        idx = np.where(sit.location.values!=' ')[0]
    else:
        idx = []
        for i in range(len(sit.location)):
            if sit.location[i]==region:
                idx.append(i)

    x = sit.year[y1:y2+1]
    y = np.nanmean(sit.sit_mean_corr[y1:y2+1,idx],axis=1)
    x = x[np.array(~np.isnan(y))]
    y = y[np.array(~np.isnan(y))]
    y = y[np.array(~np.isnan(x))]
    x = x[np.array(~np.isnan(x))]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    trend_sit = slope

    fig = px.line(x=sit.year[y1:y2+1], y=np.nanmean(sit.sit_mean_corr[y1:y2+1,idx],axis=1),markers=True,
                labels={
                    "y": "sea ice thickness (m)",
                    "x": "year"
                })
    fig.add_trace(go.Scatter(x=sit.year[y1:y2+1], y=slope*sit.year[y1:y2+1]+intercept,
                            line=dict(color='black', dash='dash'), hoverinfo='none'))
    fig.update(layout_showlegend=False)
    # add annotation
    fig.add_annotation(dict(font=dict(color='black',size=15),
                                        x=0.95,
                                        y=0.95,
                                        showarrow=False,
                                        text="Trend: "+str(np.round(trend_sit*100,2))+' cm/yr',
                                        textangle=0,
                                        xanchor='right',
                                        xref="paper",
                                        yref="paper"))

    st.plotly_chart(fig, use_container_width=True)
