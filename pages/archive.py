import streamlit as st
import numpy as np
import xarray as xr
from scipy import stats
import calendar
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m')

st.header('Proxy SIT in Canadian Arctic')
st.write("Plot proxy sea ice thickness from a Random Forest Regression using CIS ice charts and scatterometer data. Use the panels on the left to select a year (1992-2020) and a month (November-April)")



option = st.sidebar.selectbox(
    'What would you like to plot?',
    ('Sea ice thickness', 'Trends'))

if option=='Sea ice thickness':
    st.sidebar.write('Select year and month to plot')
    m = st.sidebar.select_slider('Month', options=([11,12,1,2,3,4]), help='Select a month to display')
    if m<4:
        year = st.sidebar.select_slider('Year (1993-2020)', options=(np.arange(1993,2021,1)), help='Select a year to display')
    else:
        year = st.sidebar.select_slider('Year (1992-2020)', options=(np.arange(1992,2021,1)), help='Select a year to display')



    direc = './data/'
    sit = xr.open_dataset(direc+'predic_sit_19932020_'+f"{m:02}"+'.nc')
    y = np.where(sit.year==year)[0][0]

    fig=plt.figure(dpi=200)
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-99, central_latitude=70, globe=None))
    ax.coastlines(resolution='50m',linewidth=0.5)
    ax.set_extent([-140,-57,62,84],crs=ccrs.PlateCarree())
    ax.gridlines(linewidth=0.3, color='k', alpha=0.5, linestyle=':')
    im = plt.scatter(sit.lon, sit.lat, c=sit.sit_mean[y,:].values, cmap='Spectral_r',vmin=0,vmax=3,s=9, transform=ccrs.PlateCarree())
    ax.add_feature(land_50m, facecolor='#eeeeee')
    cbar = fig.colorbar(im, ax=ax, fraction=0.029, pad=0.04,extend='max')
    cbar.ax.locator_params(nbins=7)
    cbar.ax.tick_params(labelsize=8)
    cbar.set_label(label='m',fontsize=10)
    plt.title(f'Proxy sea ice thickness ({calendar.month_name[m]} {str(year)})')

    st.pyplot(fig=fig)



if option=='Trends':
    st.sidebar.write('Select starting and end year and month to plot')
    m = st.sidebar.select_slider('Month', options=([11,12,1,2,3,4]), help='Select a month to display')
    if m<4:
        year_1,year_2 = st.sidebar.select_slider('Range years (1993-2020)', options=(np.arange(1993,2021,1)), value=[1993,2020], help='Select a starting and ending year for your trend plot')  
    else:
        year_1, year_2 = st.sidebar.select_slider('Range years (1992-2020)', options=(np.arange(1992,2021,1)), value=[1992,2020], help='Select a starting and ending year for your trend plot') 

    direc = './data/'
    sit = xr.open_dataset(direc+'predic_sit_19932020_'+f"{m:02}"+'.nc')
    sit = sit.drop(1997, dim='year')
    if m==12:
        sit = sit.drop([1993,1994,1995,1996], dim='year')

    y1 = np.where(sit.year==year_1)[0][0]
    y2 = np.where(sit.year==year_2)[0][0]

    p_value = np.zeros(sit.dims['n'])
    trend_sit = np.zeros(sit.dims['n'])
    for i in range(sit.dims['n']):
        x=sit.year[y1:y2+1]
        y=sit.sit_mean[y1:y2+1,i]

        trend_sit[i], intercept, r_value, p_value[i], std_err = stats.linregress(x, y)


#     fig=plt.figure(dpi=200)
#     ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-99, central_latitude=70, globe=None))
#     ax.coastlines(resolution='50m',linewidth=0.5)
#     ax.set_extent([-140,-57,62,84],crs=ccrs.PlateCarree())
#     ax.gridlines(linewidth=0.3, color='k', alpha=0.5, linestyle=':')
#     im = plt.scatter(sit.lon, sit.lat, c=trend_sit*100, cmap='RdBu',vmin=-3,vmax=3,s=9,transform=ccrs.PlateCarree())
#     plt.scatter(sit.lon[p_value<0.05], sit.lat[p_value<0.05], facecolors='none',
#                 s=10, edgecolor='black', linewidth=0.2, transform=ccrs.PlateCarree())
#     ax.add_feature(land_50m, facecolor='#eeeeee')
#     cbar = fig.colorbar(im,ax=ax,fraction=0.026, pad=0.04,extend='both')
#     cbar.ax.locator_params(nbins=7)
#     cbar.ax.tick_params(labelsize=8)
#     cbar.set_label(label='cm/yr',fontsize=10,fontname='Arial')
#     plt.title(f'SIT trend ({calendar.month_name[int(m)]} {str(year_1)}-{str(year_2)})', fontsize=10, fontname='Arial')

#     st.pyplot(fig=fig)


