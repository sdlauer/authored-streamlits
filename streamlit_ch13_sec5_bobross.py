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

url = "https://raw.githubusercontent.com/aimeeschwab-mccoy/streamlit_asm/main/bob_ross.csv"

bobross = pd.read_csv(url)
bobross.columns = list(bobross.columns)

col1, col2 = st.columns([2,3])

with col1:

    categorical = st.selectbox(
        "Feature",
        [
            "BARN", "BOAT", "BRIDGE", "BUILDING", "BUSHES", "CABIN", "CACTUS", "CLOUDS",
            "FARM", "FIRE", "FLOWERS", "GRASS", "LAKE", "MOON", "MOUNTAIN", "NIGHT",
            "PERSON", "RIVER", "ROCKS", "SNOW", "SUN", "TREE", "WINTER"
        ]
    )

    check = st.checkbox("Display frequency table")

    if check:
        summary = bobross.groupby(categorical).size().to_frame()
        st.dataframe(summary)

with col2:
    fig, ax = plt.subplots()

    p = sns.countplot(x=categorical, data = bobross)
    p.set_ylabel("Count")

    st.pyplot(fig)