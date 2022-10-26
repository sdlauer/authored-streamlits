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

col1, col2 = st.columns([2,3])

with col1:
    type = st.selectbox(
        "Bar chart type",
        [
            "Stacked",
            "Grouped"
        ]
    )

    grouping_1 = st.selectbox(
            "Color grouping",
            [
                "species",
                "island",
                "sex"
            ]
        )

    if (grouping_1=="species"):
        grouping_2 = st.selectbox(
            "Style grouping",
            ["island","sex"]
        )

    elif (grouping_1=="island"):
        grouping_2 = st.selectbox(
            "Style grouping",
            ["species","sex"]
        )

    elif (grouping_1=="sex"):
        grouping_2 = st.selectbox(
            "Style grouping",
            ["species","island"]
        )

    check = st.checkbox("Display cross tabulation")

    if check:
        cross = pd.crosstab(penguins[grouping_1], penguins[grouping_2])
        st.dataframe(cross)

with col2:
    fig, ax = plt.subplots()
    if type=="Stacked": sns.histplot(x=grouping_1, hue=grouping_2, data=penguins, shrink=.8, multiple="stack")
    elif type=="Grouped": sns.histplot(x=grouping_1, hue=grouping_2, data=penguins, shrink=.8, multiple="dodge")

    ax.set_xlabel(categorical, fontsize=14)
    ax.set_ylabel("Count", fontsize=14)

    st.pyplot(fig)
