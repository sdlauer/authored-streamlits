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

group = st.selectbox(
    "Grouping",
    [
        None,
        "cylinders",
        "model_year",
        "origin"
    ]
)

reg_line = st.checkbox("Regression line")
reg_eq = st.checkbox("Regression equation")
corr_coef = st.checkbox("Correlation coefficient")

fig, ax = plt.subplots()

if group==None:
    ax = sns.regplot(x=input_feat, y=output_feat,
        data=mpg, fit_reg=reg_line, ci=None, line_kws={"color": "grey"})
else:
    ax = sns.lmplot(x=input_feat, y=output_feat, hue=group,
        data=mpg)
st.pyplot(fig)
