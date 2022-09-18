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
tips.columns = ["Total bill", "Tip", "Sex", "Smoker", "Day", "Time", "Party size"]

col1, col2 = st.columns([1,3])

with col1:
    hue = st.selectbox(
        "Group by marker color",
        [
            "Day",
            "Party size",
            "Time",
            "Sex",
            "Smoker"
        ]
    )

    if hue=="Day":
            style = st.selectbox(
                "Group by marker style",
                ["Party size","Time","Sex","Smoker"]
            )

    elif hue=="Party size":
            style = st.selectbox(
                "Group by marker style",
                ["Day","Time","Sex","Smoker"]
            )

    elif hue=="Time":
            style = st.selectbox(
                "Group by marker style",
                ["Day","Party size","Sex","Smoker"]
            )

    elif hue=="Sex":
            style = st.selectbox(
                "Group by marker style",
                ["Day","Party size","Smoker","Time"]
            )

    elif hue=="Smoker":
            style = st.selectbox(
                "Group by marker style",
                ["Day","Party size","Sex","Time"]
            )

with col2:
    fig, ax = plt.subplots()

    sns.scatterplot(x="Total bill", y="Tip", data=tips,
        hue=hue, style=style)

    ax.set_xlabel(categorical, fontsize=14)
    ax.set_ylabel(numerical, fontsize=14)

    st.pyplot(fig)
