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

st.dataframe(country_sub)
