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

tips = sns.load_dataset('tips')

# st.header("Visualizing the tips dataset")

col1, col2 = st.columns([1,3])

with col1:
    plot = st.selectbox(
        "Plot",
        [
            "Box plot",
            "Density plot",
            "Violin plot",
            "Strip plot",
            "Swarm plot"
        ]
    )

    if plot != "density plot":

        categorical = st.selectbox(
            "Categorical variable",
            [
                "day",
                "time",
                "sex",
                "smoker"
            ]
        )

    numeric = st.selectbox(
        "Numeric variable",
        [
            "tip",
            "total_bill"
        ]
    )

    group = st.selectbox(
        "Grouping",
        [
            None,
            "day",
            "time",
            "sex",
            "smoker"
        ]
    )

with col2:
    fig = plt.figure()

    if plot == "Violin plot":
        sns.violinplot(x=categorical, y=numeric, hue=group, data = tips)

    elif plot == "Density plot":
        sns.kdeplot(x=numeric, hue=group, data = tips)

    elif plot == "Strip plot":
        sns.stripplot(x=categorical, y=numeric, hue=group, data = tips)

    elif plot == "Box plot":
        sns.boxplot(x=categorical, y=numeric, hue=group, data = tips)

    else:
        sns.swarmplot(x=categorical, y=numeric, hue=group, data = tips)

    st.pyplot(fig)
