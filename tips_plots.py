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


    if plot != "Density plot":
        categorical = st.selectbox(
            "Categorical variable",
            [
                "Day",
                "Party size",
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
            "Party size",
            "Time",
            "Sex",
            "Smoker"
        ]
    )

with col2:
    fig, ax = plt.subplots()

    if plot == "Violin plot":
        sns.violinplot(x=categorical, y=numeric, hue=group, data = tips)

    elif plot == "Density plot":
        sns.kdeplot(x=numeric, hue=group, multiple="stack", data = tips)

    elif plot == "Strip plot":
        sns.stripplot(x=categorical, y=numeric, hue=group, data = tips)

    elif plot == "Box plot":
        sns.boxplot(x=categorical, y=numeric, hue=group, data = tips)

    else:
        sns.swarmplot(x=categorical, y=numeric, hue=group, data = tips)

    if plot == "Density plot":
        ax.set_xlabel(numeric, fontsize=14)
        ax.set_ylabel("Density", fontsize=14)
    else:
        ax.set_xlabel(categorical, fontsize=14)
        ax.set_ylabel(numeric, fontsize=14)
        # if group != "None": ax.legend(title=group)

    st.pyplot(fig)
