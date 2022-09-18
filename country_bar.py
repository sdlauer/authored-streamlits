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

country = pd.read_csv("country_complete.csv")

# st.header("Visualizing the tips dataset")

col1, col2 = st.columns([1,3])

with col1:
    plot = st.selectbox(
        "Plot",
        [
            "Box plot",
            "Density plot",
            "Histogram"
        ]
    )

    categorical = st.selectbox(
        "Categorical feature",
        [
            "Internet access",
            "Emissions range"
        ]
    )

    continent = st.selectbox(
        "Continent",
        [
            "Africa",
            "Americas",
            "Asia",
            "Europe"
        ]
    )


with col2:
    sns.countplot(x=categorical, data=country)
    ax.set_xlabel(categorical, fontsize=14)
    ax.set_ylabel("Count", fontsize=14)
    st.pyplot(fig)
