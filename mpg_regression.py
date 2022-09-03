import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

mpg = pd.read_csv("mpg.csv")

st.title("Regression using the mpg dataset")

input_feat = st.selectbox(
    "Input feature",
    [
        "mpg",
        "horsepower",
        "displacement",
        "weight",
        "acceleration",
    ]
)

output_feat = st.selectbox(
    "Output feature",
    [
        "mpg",
        "horsepower",
        "displacement",
        "weight",
        "acceleration",
    ]
)

reg_line = st.checkbox("Regression line")
reg_eq = st.checkbox("Regression equation")
corr_coef = st.checkbox("Correlation coefficient")

fig, ax = plt.subplots()
ax = sns.regplot(x=input_feat, y=output_feat,
    data=mpg, fit_reg=reg_line, ci=None, line_kws={"color": "grey"})

st.pyplot(fig)
