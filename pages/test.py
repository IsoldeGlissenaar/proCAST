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

fig=plt.figure(dpi=200)
ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-99, central_latitude=70, globe=None))
ax.coastlines(resolution='50m',linewidth=0.5)
ax.set_extent([-140,-57,62,84],crs=ccrs.PlateCarree())
ax.gridlines(linewidth=0.3, color='k', alpha=0.5, linestyle=':')
im = plt.scatter(-120,75,c=2, cmap='Spectral_r',vmin=0,vmax=3,s=6, transform=ccrs.PlateCarree())
ax.add_feature(land_50m, facecolor='#eeeeee')
cbar = fig.colorbar(im, ax=ax, fraction=0.029, pad=0.04,extend='max')
cbar.ax.locator_params(nbins=7)
cbar.ax.tick_params(labelsize=8)
cbar.set_label(label='m',fontsize=10)
plt.title(f'Testfigure')

st.pyplot(fig=fig)
