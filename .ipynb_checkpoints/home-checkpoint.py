import streamlit as st
st.set_page_config(layout='wide')

st.header('Proxy SIT in Canadian Arctic')
st.write("A Random Forest Regression model that creates a proxy product for Canadian Arctic sea ice thickness. The dataset that is used contains parameters (stage of development and floe size) from the Canadian Ice Service charts and scatterometer backscatter. The Random Forest Regression is trained on observed CryoSat-2 sea ice thickness.")

st.write("A scientific paper about the proxy SIT product and it's validation and first results is under review and a preprint is available [here](https://egusphere.copernicus.org/preprints/2023/egusphere-2023-269/).")