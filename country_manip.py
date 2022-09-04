# import streamlit as st
# import pandas as pd
#
# country = pd.read_csv("country.csv")
#
# st.title("Manipulating the country dataset")
#
# st.subheader("Display column(s):")
# code = st.checkbox("Code", value=True)
# name = st.checkbox("Name", value=True)
# continent = st.checkbox("Continent", value=True)
# population = st.checkbox("Population", value=True)
#
# list = []
# if code: list.append("Code")
# if name: list.append("Name")
# if continent: list.append("Continent")
# if population: list.append("Population")
#
# country_sub = country[list]
#
# group = st.selectbox(
#     "Display by continent",
#     [
#         None,
#         "Asia",
#         "Europe",
#         "Africa",
#         "Oceania",
#         "North America",
#         "Antarctica",
#         "South America"
#     ]
# )
#
# if continent:
#     if group!=None:
#         country_sub = country_sub[country_sub["Continent"] == group]
#         st.dataframe(country_sub)
#         st.subheader("Mean population of all countries in " + group)
#         st.text(country_sub.mean().round(0))
#     elif group==None:
#         st.dataframe(country_sub)
#         st.subheader("Mean population of all countries")
#         st.text(country_sub.mean().round(0))
# else:
#     st.dataframe(country_sub)

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

country = pd.read_csv("country.csv")

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection


country = pd.read_csv("country.csv")

selection = aggrid_interactive_table(df=iris)

if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])
