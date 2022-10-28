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
    feature = st.selectbox(
        "Display rows with missing values for the selected feature",
        ["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]
    )

with col2:
    penguins[penguins[feature].isna()]
