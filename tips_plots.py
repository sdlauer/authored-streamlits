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
            "Strip plot",
            "Swarm plot",
            "Violin plot"
        ]
    )

    if plot != "Density plot":

        categorical = st.selectbox(
            "Categorical variable",
            [
                "Day",
                "Time",
                "Sex",
                "Smoker"
            ]
        )

    numeric = st.selectbox(
        "Numeric variable",
        [
            "Tip",
            "Total bill"
        ]
    )

    group = st.selectbox(
        "Grouping",
        [
            None,
            "Day",
            "Time",
            "Sex",
            "Smoker"
        ]
    )

dict_cat = {
  "Day": "day",
  "Time": "time",
  "Sex": "sex",
  "Smoker": "smoker"
}

dict_num = {
  "Tip": "tip",
  "Total bill": "total_bill"
}

with col2:
    fig = plt.figure()

    if plot == "Violin plot":
        sns.violinplot(x=categorical[dict_cat], y=numeric[dict_num], hue=group[dict_cat], data = tips)

    elif plot == "Density plot":
        sns.kdeplot(x=numeric[dict_num], hue=group, data = tips)

    elif plot == "Strip plot":
        sns.stripplot(x=categorical[dict_cat], y=numeric[dict_num], hue=group[dict_cat], data = tips)

    elif plot == "Box plot":
        sns.boxplot(x=categorical[dict_cat], y=numeric[dict_num], hue=group[dict_cat], data = tips)

    else:
        sns.swarmplot(x=categorical[dict_cat], y=numeric[dict_num], hue=group[dict_cat], data = tips)

    st.pyplot(fig)
