import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

st.header("Visualizing the tips dataset")
plot = st.selectbox(
    "Plot",
    [
        "violin plot",
        "strip plot",
        "box plot",
        "swarm plot"
    ]
)

categorical = st.selectbox(
    "Categorical variable",
    [
        "day",
        "time",
        "sex",
        "smoker"
    ]
)

numeric = st.selectbox(
    "Numeric variable",
    [
        "tip",
        "total_bill"
    ]
)

group = st.selectbox(
    "Grouping",
    [
        None,
        "day",
        "time",
        "sex",
        "smoker"
    ]
)

fig = plt.figure()

if plot == "violin plot":
    sns.violinplot(x=categorical, y=numeric, data = tips)

elif plot == "strip plot":
    sns.stripplot(x=categorical, y=numeric, data = tips)

elif plot == "box plot":
    sns.boxplot(x=categorical, y=numeric, data = tips)

else:
    sns.swarmplot(x=categorical, y=numeric, data = tips)

st.pyplot(fig)
