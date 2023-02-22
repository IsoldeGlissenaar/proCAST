import streamlit as st


st.header('About the SIT proxy product')
st.write("The sea ice thickness proxy product was created using [Canadian Ice Service](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/about-ice-service.html) ice charts and a Random Forest Regression. The sea ice thickness proxy product is available for the winter months November-April. The archive of historical proxy sea ice thickness is available from 1996. Operational proxy sea ice thickness maps will be released weekly.")

st.subheader("Frequently Asked Questions")

with st.expander("What is a Random Forest Regression?"):
    st.write("A Random Forest Regression is a supervised machine learning algorithm. It combines predictions from multiple decision tree algorithms to make a more accurate prediction than a single model. Read more [here](https://towardsdatascience.com/random-forest-regression-5f605132d19d).")

with st.expander("What are ice charts?"):
    st.write("Ice charts are maps of the sea ice that illustrate ice conditions at a particular moment in time. The Canadian Ice Service publishes ice charts for the Canadian Arctic straits, seas and oceans, to serve tactical or strategic planning and operational purposes.")
    st.write("The regional ice charts show the ice conditions for a given region valid on Mondays. They are based on an analysis and integration of data from: satellite imagery, weather and oceanographic information, visual observations from ship and aircraft. The charts indicate the concentration in tenths, stage of development and form of ice. Click [here](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/latest-conditions/products-guides/chart-descriptions.html) for more information.")
    
with st.expander("When will a new proxy SIT map be released?"):
    st.write("The Canadian Ice Service releases their regional ice charts on a weekly basis. These ice charts are constructed for information available on Monday and released on Wednesday. The operational page on this website is update every Thursday morning (UTC), releasing the new operational SIT proxy map.")