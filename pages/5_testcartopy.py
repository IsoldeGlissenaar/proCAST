import sys
sys.path.append('./suboptions/')
import figs
import timeline
import streamlit as st
import numpy as np
import xarray as xr
from scipy import stats
import plotly.graph_objects as go
import calendar
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m')

st.write("Test cartopy")


fig=plt.figure()
ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-99, central_latitude=70, globe=None))
ax.coastlines(resolution='50m',linewidth=0.5)
ax.set_extent([-140,-57,62,84],crs=ccrs.PlateCarree())
ax.gridlines(linewidth=0.3, color='k', alpha=0.5, linestyle=':')
ax.add_feature(land_50m, facecolor='#eeeeee')
plt.title(f'Proxy sea ice thickness ({calendar.month_name[m]} {str(year)})')

st.pyplot(fig=fig)





