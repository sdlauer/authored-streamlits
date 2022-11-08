import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import t

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
            "binomial",
            "normal",
            "t"
        ]
    )
    st.text("Enter value or use - and +")
    if distribution == "binomial":
        nobs = st.number_input(
            "n",
            min_value=1,
            step=1,
            value=10
        )
        prob = st.number_input(
            label="Probability",
            min_value=0.00,
            max_value=1.00,
            value=0.50,
            step=0.01
        )
    elif distribution == "normal":
        meanmu = st.number_input(
            "Mean",
            value=0.0,
            step=0.1
        )
        stsigma = st.number_input(
            "Standard deviation",
            min_value=0.00,
            value=1.00,
            step=0.01
        )
    else:
        df = st.number_input(
            "Degrees of freedom (df)",
            min_value=0,
            step=1,
            value=10
        )
with col2:
    fig, ax = plt.subplots()
    if distribution == "binomial":
        x = range(0, int(nobs)+1)
        ax.bar(x, height=binom.pmf(k=x, n=nobs, p=prob), width=0.75)
        ax.set(xlabel='X', ylabel="Probability")
        ax.title.set_text("binomial( %02d, %0.2f)" %(nobs, prob))
    elif distribution == "normal":
        x = np.linspace(normal.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
        ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma))
        ax.set(xlabel='X', ylabel='Density')
        ax.title.set_text('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
    else:
        x = np.linspace(t.ppf(0.0001, df=df), t.ppf(0.9999, df), 100)
        ax.plot(x, t.pdf(x=x, df=df))
        ax.set(xlabel='X', ylabel='Density')
        ax.title.set_text('t(%02d)' %df)

    st.pyplot(fig)
   

