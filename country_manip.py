import streamlit as st
import pandas as pd

country = pd.read_csv("country.csv")

st.title("Manipulating the country dataset")

code = st.checkbox("Code")
name = st.checkbox("Name")
continent = st.checkbox("Continent")
population = st.checkbox("Population")

list = []
if code: list.append()
if name: list.append()
if continent: list.append()
if population: list.append()

country_sub = country[list]

st.dataframe(country_sub)
