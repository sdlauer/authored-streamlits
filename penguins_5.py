import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {overflow: hidden;}
        div.block-container {padding-top:1rem;}
        div.block-container {padding-bottom:1rem;}
        </style>
        """
st.markdown(hide, unsafe_allow_html=True)

penguins = sns.load_dataset('penguins')
penguins.columns = ["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]

col1, col2 = st.columns([1.5,3])

with col1:
    columns = st.multiselect(
    'Select features',
    ["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"],
    ["species", "island"])

    feature = st.selectbox(
        "Display rows with missing values for the selected feature",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]
    )

with col2:
    st.write(penguins[columns])
#    if feature: st.write((penguins[penguins[feature].isna()]))
