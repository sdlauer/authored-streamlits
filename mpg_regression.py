import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Regression using the mpg dataset")

mpg = pd.read_csv("mpg.csv")

reg_line = st.checkbox("Regression line")
reg_eq = st.checkbox("Regression equation")
corr_coef = st.checkbox("Correlation coefficient")

input = st.selectbox(
    "Input feature",
    [
        'mpg',
        'cylinders',
        'displacement',
        'horsepower',
        'weight',
        'acceleration',
        'model_year',
        'origin',
        'name'
    ]
)

output = st.selectbox(
    "Output feature",
    [
        'mpg',
        'cylinders',
        'displacement',
        'horsepower',
        'weight',
        'acceleration',
        'model_year',
        'origin',
        'name'
    ]
)

fig = plt.figure()
sns.violinplot(x=input, y=output, data=mpg)
st.pyplot(fig)
