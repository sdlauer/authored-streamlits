import streamlit as st
import pandas as pd

country = pd.read_csv("country.csv")

code = st.checkbox("Code")
name = st.checkbox("Name")
continent = st.checkbox("Continent")
population = st.checkbox("Population")

st.title("Manipulating the country dataset")
