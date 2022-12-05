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
    plot = st.selectbox(
        "Plot",
        [
            "Box plot",
            "Violin plot",
            "Strip plot",
            "Swarm plot"
        ]
    )

    numerical = st.selectbox(
        "Numerical feature",
        [
            "Tip",
            "Total bill"
        ]
    )


    categorical = st.selectbox(
        "Categorical feature",
        [
            "Day",
            "Party size",
            "Time",
            "Sex",
            "Smoker"
        ]
    )

    if (categorical=="Day"):
            group = st.selectbox(
                "Grouping",
                ["Party size","Time","Sex","Smoker"]
            )

    elif (categorical=="Party size"):
            group = st.selectbox(
                "Grouping",
                ["Day","Time","Sex","Smoker"]
            )

    elif (categorical=="Time"):
            group = st.selectbox(
                "Grouping",
                ["Day","Party size","Sex","Smoker"]
            )

    elif (categorical=="Sex"):
            group = st.selectbox(
                "Grouping",
                ["Day","Party size","Smoker","Time"]
            )

    elif (categorical=="Smoker"):
            group = st.selectbox(
                "Grouping",
                ["Day","Party size","Sex","Time"]
            )

with col2:
    fig, ax = plt.subplots()

    if plot == "Violin plot":
        sns.violinplot(x=categorical, y=numerical, hue=group, data = tips)

    elif plot == "Strip plot":
        sns.stripplot(x=categorical, y=numerical,  hue=group, data = tips)

    elif plot == "Box plot":
        sns.boxplot(x=categorical, y=numerical,  hue=group, data = tips)

    else:
        sns.swarmplot(x=categorical, y=numerical,  hue=group, data = tips)

    ax.set_xlabel(categorical, fontsize=14)
    ax.set_ylabel(numerical, fontsize=14)

    st.pyplot(fig)
