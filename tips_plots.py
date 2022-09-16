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

    # group = st.selectbox(
    #     "Grouping",
    #     [
    #         "None",
    #         "Day",
    #         "Time",
    #         "Sex",
    #         "Smoker"
    #     ]
    # )

dict = {
  "None": None,
  "Day": "day",
  "Time": "time",
  "Sex": "sex",
  "Smoker": "smoker",
  "Tip": "tip",
  "Total bill": "total_bill"
}

with col2:
    fig, ax = plt.subplots()

    if plot == "Violin plot":
        sns.violinplot(x=dict[categorical], y=dict[numeric], data = tips)

    elif plot == "Density plot":
        sns.kdeplot(x=dict[numeric], hue=dict[categorical], data = tips)

    elif plot == "Strip plot":
        sns.stripplot(x=dict[categorical], y=dict[numeric], data = tips)

    elif plot == "Box plot":
        sns.boxplot(x=dict[categorical], y=dict[numeric], data = tips)

    else:
        sns.swarmplot(x=dict[categorical], y=dict[numeric], data = tips)

    if plot == "Density plot":
        ax.set_xlabel(numeric, fontsize=14)
        ax.set_ylabel("Density", fontsize=14)
        ax.legend(title=categorical)
    else:
        ax.set_xlabel(categorical, fontsize=14)
        ax.set_ylabel(numeric, fontsize=14)

    st.pyplot(fig)
