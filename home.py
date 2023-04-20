import streamlit as st
st.set_page_config(layout='wide', initial_sidebar_state="expanded")

st.header('Proxy sea ice thickness in the Canadian Arctic')

col1, col2 = st.columns(2)

with col1:
    st.write("Sea ice thickness is a key variable when characterising an ice cover and its impact on the local environment, for safety for shipping and offshore construction, and provides important insight into how an ice cover is changing in response to climate change. Unfortunately, observations of ice thickness at appropriate spatial and temporal scales are sparse, especially in the channels in the Canadian Arctic Archipelago.  \nThis project aims to create a long-term proxy record of winter sea ice thickness for the Canadian Arctic, being updated on a weekly basis.")
    st.write("The Canadian Arctic sea ice thickness proxy product was created by applying machine learning techniques to ice charts from the Canadian Ice Service. After comparing multiple models, a Random Regression Model was found to give the best results. CryoSat-2 observed sea ice thickness was used as reference to train the model on. The model was validated using BGEP moorings in the Beaufort Sea, ECCC ice stake observations at weather stations in the Canadian Arctic Archipelago, and Operation IceBridge airborne observations.")
    
with col2:
    st.image("image/locations_charts.png", width=500)

st.write("A scientific paper about the proxy SIT product and it's validation and first results is under review and a preprint is available [here](https://egusphere.copernicus.org/preprints/2023/egusphere-2023-269/).")
st.write("Check out the [latest ice conditions](https://canadian-sit.streamlit.app/latest).")

st.image("image/ship_arctic.jpg", caption="Photo Credit: Patrick Kelley, U.S. Coast Guard")

st.write("When using the data please refer to these sources:  \n Glissenaar, I., Landy, J., Babb, D., Dawson, G. & Howell, S. (2023). IsoldeGlissenaar/CanadianSITproxy: Proxy SIT Canadian Arctic - dataset (v0.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7712970  \nGlissenaar, I. A., Landy, J. C., Babb, D. G., Dawson, G. J., and Howell, S. E. L.: A long-term proxy for sea ice thickness in the Canadian Arctic: 1996–2020, EGUsphere [preprint], https://doi.org/10.5194/egusphere-2023-269, 2023.")