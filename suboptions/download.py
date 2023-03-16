import tempfile
from zipfile import ZipFile

import streamlit as st


def save_shapefile_with_bytesio(dataframe,directory,date):
    dataframe.to_file(f"{directory}/{date}_CanadianArctic_chart_SIT.shp",  driver='ESRI Shapefile')
    zipObj = ZipFile(f"{directory}/{date}_CanadianArctic_chart_SIT.zip", 'w')
    zipObj.write(f"{directory}/{date}_CanadianArctic_chart_SIT.shp",arcname = 'user_shapefiles.shp')
    zipObj.write(f"{directory}/{date}_CanadianArctic_chart_SIT.cpg",arcname = 'user_shapefiles.cpg')
    zipObj.write(f"{directory}/{date}_CanadianArctic_chart_SIT.dbf",arcname = 'user_shapefiles.dbf')
    zipObj.write(f"{directory}/{date}_CanadianArctic_chart_SIT.prj",arcname = 'user_shapefiles.prj')
    zipObj.write(f"{directory}/{date}_CanadianArctic_chart_SIT.shx",arcname = 'user_shapefiles.shx')
    zipObj.close()

def add_downloadbutton_shp(date, dataset):
    #download the geodataframe
    #we first create a temporary directory
    with tempfile.TemporaryDirectory() as tmp:
        #create the shape files in the temporary directory
        save_shapefile_with_bytesio(dataset,tmp,date)
        with open(f"{tmp}/{date}_CanadianArctic_chart_SIT.zip", "rb") as file:
            st.download_button(
                label="Download recent conditions",
                data=file,
                file_name=date+"_CanadianArctic_chart_SIT.zip",
                mime='application/zip',
            )
