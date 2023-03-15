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

st.write("Test matplotlib")

fig = plt.figure()
plt.scatter([0,1],[0,1])
st.pyplot(fig=fig)



