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
col1, col2 = st.columns([1,3])

with col1:
    numerical_1 = st.selectbox(
        "First numerical feature",
        [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g"
        ]
    )

    if (numerical_1=="bill_length_mm"):
            numerical_2 = st.selectbox(
                "Second numerical feature",
                ["bill_depth_mm", "flipper_length_mm", "body_mass_g"]
            )

    elif (numerical_1=="bill_depth_mm"):
            numerical_2 = st.selectbox(
                "Second numerical feature",
                ["bill_length_mm", "flipper_length_mm", "body_mass_g"]
            )

    elif (numerical_1=="flipper_length_mm"):
            numerical_2 = st.selectbox(
                "Second numerical feature",
                ["bill_length_mm", "bill_depth_mm", "body_mass_g"]
            )

    elif (numerical_1=="body_mass_g"):
            numerical_2 = st.selectbox(
                "Second numerical feature",
                ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
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

with col2:
    fig, ax = plt.subplots()
    sns.scatterplot(x=numerical_1, y=numerical_2, hue=grouping_1, style=grouping_2, data = penguins)
    ax.set_xlabel(numerical_1, fontsize=14)
    ax.set_ylabel(numerical_2, fontsize=14)
    st.pyplot(fig)
