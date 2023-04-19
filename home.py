import streamlit as st
st.set_page_config(layout='wide')

st.header('Proxy SIT in Canadian Arctic')
st.write("A Random Forest Regression model that creates a proxy product for Canadian Arctic sea ice thickness. The dataset that is used contains parameters (stage of development and floe size) from the Canadian Ice Service charts and scatterometer backscatter. The Random Forest Regression is trained on observed CryoSat-2 sea ice thickness.")

st.write("A scientific paper about the proxy SIT product and it's validation and first results is under review and a preprint is available [here](https://egusphere.copernicus.org/preprints/2023/egusphere-2023-269/).")

st.image("image/ship_arctic.jpg", caption="Photo Credit: Patrick Kelley, U.S. Coast Guard")

st.write("When using the data please use these citations:  \n Glissenaar, I., Landy, J., Babb, D., Dawson, G. & Howell, S. (2023). IsoldeGlissenaar/CanadianSITproxy: Proxy SIT Canadian Arctic - dataset (v0.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7712970  \nGlissenaar, I. A., Landy, J. C., Babb, D. G., Dawson, G. J., and Howell, S. E. L.: A long-term proxy for sea ice thickness in the Canadian Arctic: 1996–2020, EGUsphere [preprint], https://doi.org/10.5194/egusphere-2023-269, 2023.")