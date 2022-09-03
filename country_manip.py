import streamlit as st
import pandas as pd

country = pd.read_csv("country.csv")

st.title("Manipulating the country dataset")

code = st.checkbox("Code", value=True)
name = st.checkbox("Name", value=True)
continent = st.checkbox("Continent", value=True)
population = st.checkbox("Population", value=True)

list = []
if code: list.append("Code")
if name: list.append("Name")
if continent: list.append("Continent")
if population: list.append("Population")

country_sub = country[list]

group = st.selectbox(
    "Group by continent",
    [
        None,
        "Asia",
        "Europe",
        "Africa",
        "Oceania",
        "North America",
        "Antarctica",
        "South America"
    ]
)

if continent:
    if group!=None:
        country_sub = country_sub[country_sub["Continent"] == group]
        st.dataframe(country_sub)
        st.subheader("Mean population of all countries in " + group)
        st.text(country_sub.mean().round(0))
    elif group==None:
        st.dataframe(country_sub)
        st.subheader("Mean population of all countries")
        st.text(country_sub.mean().round(0))
else:
    st.dataframe(country_sub)
