import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
hide_st_style = “”"

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

“”"
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)

tips = sns.load_dataset('tips')

st.header("Visualizing the tips dataset")

col1, col2 = st.columns([1,3])

with col1:
    plot = st.selectbox(
        "Plot",
        [
            "violin plot",
            "strip plot",
            "box plot",
            "swarm plot"
        ]
    )

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

    if plot == "violin plot":
        sns.violinplot(x=categorical, y=numeric, hue=group, data = tips)

    elif plot == "strip plot":
        sns.stripplot(x=categorical, y=numeric, hue=group, data = tips)

    elif plot == "box plot":
        sns.boxplot(x=categorical, y=numeric, hue=group, data = tips)

    else:
        sns.swarmplot(x=categorical, y=numeric, hue=group, data = tips)

    st.pyplot(fig)
