import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

mpg=pd.read_csv("mpg.csv")

st.title("Regression using the mpg dataset")

input_feat = st.selectbox(
    "Input feature",
    [
        "mpg",
        "displacement",
        "horsepower",
        "weight",
        "acceleration",
    ]
)

output_feat = st.selectbox(
    "Output feature",
    [
        "mpg",
        "displacement",
        "horsepower",
        "weight",
        "acceleration",
    ]
)

reg_line = st.checkbox("Regression line")
reg_eq = st.checkbox("Regression equation")
corr_coef = st.checkbox("Correlation coefficient")

fig = plt.figure()
sns.scatterplot(x=input_feat, y=output_feat, data=mpg)
st.pyplot(fig)
