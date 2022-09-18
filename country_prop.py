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
    categorical = st.selectbox(
        "Categorical feature",
        [
            "Continent",
            "Internet access",
            "Emissions range"
        ]
    )

    counts = country[["Country",categorical]].groupby(categorical).count()
    counts.columns = ["Count"]
    counts.insert(2, "Proportion", df["Count"]/151, True)
    st.dataframe(counts)

with col2:
    fig, ax = plt.subplots()

    sns.histplot(x=categorical, data=country, shrink=.8)
    ax.set_xlabel(categorical, fontsize=14)
    ax.set_ylabel("Count", fontsize=14)
    st.pyplot(fig)
