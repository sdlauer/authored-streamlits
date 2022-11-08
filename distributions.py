import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

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

col1, col2 = st.columns([2,3])

with col1:
    distribution  =st.selectbox(
        "Distribution",
        [
            "Binomial",
            "normal"
            "t"
        ]
    )

    if distribution == "Binomial":
        nobs = st.number_input(
            "n",
            min_value=1,
            step=1,
            value=10
        )
        prob = st.number_input(
            "Probability of success",
            min_value=0,
            max_value=1,
            value=0.5,
            step=0.01
        )
    elif distribution == "normal":
        meanmu = st.number_input(
            "Mean",
            value=0,
            step=0.1
        )
        stsigma = st.number_input(
            "Standard deviation",
            min_value=0,
            value=1,
            step=0.01
        )
    else:
        df = st.number_input(
            "Degrees of freedom (df)",
            min_value=0,
            step=1,
            value=10
        )


