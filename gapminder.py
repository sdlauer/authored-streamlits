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

gapminder = pd.read_csv("gapminder.csv")

# st.header("Visualizing the tips dataset")

col1, col2 = st.columns([1,3])

with col1:
    plot = st.selectbox(
        "Plot",
        [
            "Box plot",
            "Histogram"
        ]
    )

    numerical = st.selectbox(
        "Numerical feature",
        [
            "Population",
            "GDP",
            "Life expectancy"
        ]
    )


with col2:
    fig, ax = plt.subplots()

    if plot == "Box plot":
        sns.boxplot(x=numerical, data=gapminder)

    elif plot == "Histogram":
        sns.histplot(x=numerical, data=gapminder)

    ax.set_xlabel(numerical, fontsize=14)
    ax.ticklabel_format(style='plain', axis='x')
    if numerical=="Population": ax.tick_params(axis='x', labelrotation = 30)

    st.pyplot(fig)
