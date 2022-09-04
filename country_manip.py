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

st.set_page_config(
    layout="centered"
)

st.header("Manipulating the country dataset")
instructions = "Clicking Filters "
col_ins = "Click Columns to display specific columns in the country dataset."
row_ins = "Click Filters to display rows that satisfy a specific condition. "
row_ex1 = "Ex: Clicking Population and selecting less than and typing 1000000 "
row_ex2 = "returns rows where the population column is less than 1000000."
piv1 = "Toggling Pivot Mode under Columns calculates various summary "
piv2 = "statistics such as average population of countries in each continent."

st.write(row_ins + row_ex1 + row_ex2)
st.write(col_ins)
st.write(piv1 + piv2)


def aggrid_interactive_table(df: pd.DataFrame):
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        height=400,
        gridOptions=options.build(),
        theme="blue",
        update_mode=GridUpdateMode.MODEL_CHANGED,
    )

    return selection


country = pd.read_csv(
    "country.csv"
)

selection = aggrid_interactive_table(df=country)

if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])
