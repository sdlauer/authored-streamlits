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

passenger = pd.read_csv('DataScienceFoundations/passenger.csv')
passenger.columns = ["ID", "License", "Cost", "TotalTime", "Satisfaction"]

col1, col2 = st.columns([2,3])

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

    numerical = st.selectbox(
        "Numerical feature",
        [
            "Cost",
            "TotalTime"
        ]
    )

    categorical = st.selectbox(
        "Categorical feature",
        [
            "License",
            "Satisfaction",
        ]
    )

    check = st.checkbox("Display summary statistics")

    if check:
        summary = passenger.groupby(categorical)[numerical].describe()
        summary.columns = ["Count","Mean","Std", "Min", "Q1", "Median", "Q3", "Max"]
        summary = summary[["Min", "Q1", "Median", "Q3", "Max"]]
        st.dataframe(summary)

with col2:
    fig, ax = plt.subplots()

    if plot == "Violin plot":
        sns.violinplot(x=categorical, y=numerical, data = passenger)

    elif plot == "Density plot":
        sns.kdeplot(x=numerical, multiple="stack", hue=categorical, data = passenger)

    elif plot == "Strip plot":
        sns.stripplot(x=categorical, y=numerical, data = passenger)

    elif plot == "Box plot":
        sns.boxplot(x=categorical, y=numerical, data = passenger)

    else:
        sns.swarmplot(x=categorical, y=numerical, data = passenger)

    if plot == "Density plot":
        ax.set_xlabel(numerical, fontsize=14)
        ax.set_ylabel("Density", fontsize=14)
    else:
        ax.set_xlabel(categorical, fontsize=14)
        ax.set_ylabel(numerical, fontsize=14)

    st.pyplot(fig)