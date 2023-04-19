import sys
sys.path.append('./suboptions/')

import numpy as np
import streamlit as st

import figs
import timeline


st.header('Proxy SIT in Canadian Arctic')
st.write("The proxy sea ice thickness archive inlcudes sea ice thickness for November-April for the period 1996-2020. The archive uses both data from the CIS ice charts and scatterometer data (the latter not being used in the weekly 'latest' product as it is not released on an operational basis).")

option = st.selectbox(
    'What would you like to plot?',
    ('Sea ice thickness', 'Trends'))

if option=='Sea ice thickness':
    st.write('Select year and month to plot')
    m = st.select_slider('Month', options=([11,12,1,2,3,4]), help='Select a month to display')
    year = st.select_slider('Year (1996-2020)',
                            options=(np.arange(1996,2021,1)),
                            help='Select a year to display')
    figs.sitfig(m,year)

if option=='Trends':
    st.write('Select starting and end year and month to plot')
    m = st.select_slider('Month', options=([11,12,1,2,3,4]), help='Select a month to display')
    year_1, year_2 = st.select_slider('Range years (1996-2020)',
                                    options=(np.arange(1996,2021,1)),
                                    value=[1996,2020],
                                    help='Select a starting and ending year for your trend plot')
    timeline.sittrendfig(m,year_1,year_2)

    # Plot timeline SIT for a given region
    st.write('Plot timeline and trend SIT for a given region:')
    location = st.selectbox(
        'Location',
        ('Full area', 'Arctic Ocean Periphery', 'Baffin Bay', 'Beaufort Sea', 'Parry Channel'))
    timeline.timeline(m,year_1,year_2, location)
