import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

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

st.header("Linear regression with the cars dataset")

col1, col2 = st.columns([1,3])

with col1:

    input_feat = st.selectbox(
        "Input feature",
        [
            "mpg",
            "cylinders",
            "horsepower",
            "displacement",
            "weight",
            "acceleration",
            "model_year"
        ]
    )

    output_feat = st.selectbox(
        "Output feature",
        [
            "mpg",
            "cylinders",
            "horsepower",
            "displacement",
            "weight",
            "acceleration",
            "model_year"
        ]
    )

    reg_line = st.checkbox("Regression line")
    reg_eq = st.checkbox("Regression equation")
    corr_coef = st.checkbox("Correlation coefficient")

with col2:

    fig, ax = plt.subplots()

    ax = sns.regplot(x=input_feat, y=output_feat,
        data=mpg, fit_reg=reg_line, ci=None, line_kws={"color": "grey"})

    # st.subheader("Scatter plot")
    st.pyplot(fig)

    if reg_eq:
        st.subheader("Regression equation")
        st.text(show_eq([mpg[input_feat],mpg[output_feat]]))

    if corr_coef:
        st.subheader("Correlation coefficient")
        st.text(show_corr([mpg[input_feat],mpg[output_feat]]))
