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


penguins.columns = ["Species", "Island", "Bill length", "Bill depth", "Flipper length", "Body mass", "Sex"]

col1, col2 = st.columns([1,3])

with col1:
    categorical_1 = st.selectbox(
        "Select numerical feature",
        [
            "Bill length",
            "Bill depth",
            "Flipper length",
            "Body mass"
        ]
    )

    if (categorical_1=="Bill length"):
            categorical_2 = st.selectbox(
                "Select another numerical feature",
                ["Bill depth", "Flipper length", "Body mass"]
            )

    elif (categorical_1=="Bill depth"):
            categorical_2 = st.selectbox(
                "Select another numerical feature",
                ["Bill length", "Flipper length", "Body mass"]
            )

    elif (categorical_1=="Flipper length"):
            categorical_2 = st.selectbox(
                "Select another numerical feature",
                ["Bill length", "Bill depth", "Body mass"]
            )

    elif (categorical_1=="Body mass"):
            categorical_2 = st.selectbox(
                "Select another numerical feature",
                ["Bill length", "Bill depth", "Flipper length"]
            )

    grouping_1 = st.selectbox(
            "Select color grouping",
            [
                "Species",
                "Island",
                "Sex"
            ]
        )

    if (grouping_1=="Species"):
        grouping_2 = st.selectbox(
            "Select style grouping",
            ["Island","Sex"]
        )

    elif (grouping_1=="Island"):
        grouping_2 = st.selectbox(
            "Select style grouping",
            ["Species","Sex"]
        )

    elif (grouping_1=="Sex"):
        grouping_2 = st.selectbox(
            "Select style grouping",
            ["Species","Island"]
        )

with col2:
    fig, ax = plt.subplots()
    sns.scatterplot(x=categorical_1, y=categorical_2, hue=grouping_1, stype=grouping_2, data = penguins)
    ax.set_xlabel(categorical_1, fontsize=14)
    ax.set_ylabel(categorical_2, fontsize=14)
    st.pyplot(fig)
