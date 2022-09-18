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

    type = st.selectbox(
        "Categorical feature",
        [
            "Stacked",
            "Grouped"
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

    if categorical=="Day":
            group = st.selectbox(
                "Grouping",
                ["Party size","Time","Sex","Smoker"]
            )

    elif categorical=="Party size":
            group = st.selectbox(
                "Grouping",
                ["Day","Time","Sex","Smoker"]
            )

    elif categorical=="Time":
            group = st.selectbox(
                "Grouping",
                ["Day","Party size","Sex","Smoker"]
            )

    elif categorical=="Sex":
            group = st.selectbox(
                "Grouping",
                ["Day","Party size","Smoker","Time"]
            )

    else:
            group = st.selectbox(
                "Grouping",
                ["Day","Party size","Sex","Time"]
            )

    check = st.checkbox("Display cross tabulation")
    if check:
        cross = pd.crosstab(tips["categorical"], tips["group"])
        st.dataframe(cross)

with col2:
    fig, ax = plt.subplots()
    if type=="Stacked": sns.histplot(x=categorical, hue=group, data=tips, shrink=.8, multiple="stack")
    elif type=="Grouped": sns.histplot(x=categorical, hue=group, data=tips, shrink=.8, multiple="dodge")

    ax.set_xlabel(categorical, fontsize=14)
    ax.set_ylabel("Count", fontsize=14)

    st.pyplot(fig)
