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

# st.header("Linear regression with the cars dataset")

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

dict = {
  "mpg": "MPG",
  "cylinders": "Cylinders",
  "horsepower": "Horsepower",
  "displacement": "Displacement",
  "weight": "Weight",
  "acceleration": "Acceleration",
  "model_year": "Model year"
}

#    reg_line = st.checkbox("Regression line")
#    reg_eq = st.checkbox("Regression equation")
#    corr_coef = st.checkbox("Correlation coefficient")

with col2:

    fig, ax = plt.subplots()

#    ax = sns.regplot(x=input_feat, y=output_feat,
#        data=mpg, fit_reg=reg_line, ci=None, line_kws={"color": "grey"})

    ax = sns.regplot(x=input_feat, y=output_feat,
        data=mpg, fit_reg=False, ci=None, line_kws={"color": "grey"})
    ax.set_xlabel(dict[input_feat], fontsize=14)
    ax.set_ylabel(dict[output_feat], fontsize=14)

    # st.subheader("Scatter plot")
    st.pyplot(fig)

    # if reg_eq:
    #     # st.subheader("Regression equation")
    #     st.text("Regression equation: "
    #         + show_eq([mpg[input_feat],mpg[output_feat]]))
    #
    # if corr_coef:
    #     # st.subheader("Correlation coefficient")
    #     st.text("Correlation coefficient: "
    #         + show_corr([mpg[input_feat],mpg[output_feat]]))
