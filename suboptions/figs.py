import calendar

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import xarray as xr

land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m')


def sitfig(m,year):
    direc = './data/'
    sit = xr.open_dataset(direc+'proxy_sit_canadianarctic_19962020_'+f"{m:02}"+'.nc')
    y = np.where(sit.year==year)[0][0]

    fig = plt.figure()
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-99, central_latitude=70, globe=None))
    ax.coastlines(resolution='50m',linewidth=0.5)
    ax.set_extent([-140,-57,62,84],crs=ccrs.PlateCarree())
    ax.gridlines(linewidth=0.3, color='k', alpha=0.5, linestyle=':')
    im = plt.scatter(sit.lon, sit.lat, c=sit.sit_mean[y,:].values,
                    cmap='Spectral_r',vmin=0,vmax=3,s=9, transform=ccrs.PlateCarree())
    ax.add_feature(land_50m, facecolor='#eeeeee')
    cbar = fig.colorbar(im, ax=ax, fraction=0.029, pad=0.04,extend='max')
    cbar.ax.locator_params(nbins=7)
    cbar.ax.tick_params(labelsize=8)
    cbar.set_label(label='m',fontsize=10)
    plt.title(f'Proxy sea ice thickness ({calendar.month_name[m]} {str(year)})')
    st.pyplot(fig=fig)
