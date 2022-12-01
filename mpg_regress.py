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
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """

st.markdown(hide, unsafe_allow_html=True)

# Load dataset
mpg = pd.read_csv("mpg.csv")

# Functions for equation and correlation
def show_eq(data):
    m, b = np.polyfit(data[0], data[1], 1)
    m = round(m,3)
    b = round(b,3)
    eq = 'y = ' + str(m) + 'x + ' + str(b)
    return eq

def show_corr(data):
    # Note: np.corrcoef gives a correlation matrix
    corr_coef = np.corrcoef(data[0],data[1])
    corr_coef = round(corr_coef[0,1],3)
    corr = 'r = ' + str(corr_coef)
    return corr

tab1, tab2 = st.tabs(["Plot", "Data"])

with tab1:
    col1, col2 = st.columns([1,3])
    with col1:

        input_feat = st.selectbox(
            "Input feature",
            [
                "MPG",
                "Cylinders",
                "Horsepower",
                "Displacement",
                "Weight",
                "Acceleration",
                "Model year"
            ]
        )

        output_feat = st.selectbox(
            "Output feature",
            [
                "MPG",
                "Cylinders",
                "Horsepower",
                "Displacement",
                "Weight",
                "Acceleration",
                "Model year"
            ]
        )

    dict = {
      "MPG": "mpg",
      "Cylinders": "cylinders",
      "Horsepower": "horsepower",
      "Displacement": "displacement",
      "Weight": "weight",
      "Acceleration": "acceleration",
      "Model year": "model_year"
    }

    with col2:

        fig, ax = plt.subplots()
        ax = sns.regplot(x=dict[input_feat], y=dict[output_feat],
            data=mpg, fit_reg=False, ci=None, line_kws={"color": "grey"})
        ax.set_xlabel(input_feat, fontsize=14)
        ax.set_ylabel(output_feat, fontsize=14)
        st.pyplot(fig)

with tab2:
    st.table(mpg[[dict[input_feat],dict[output_feat]])
