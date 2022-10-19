import streamlit as st
import pandas as pd
#import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
#from sklearn.preprocessing import PolynomialFeatures

# Import and view the dataset
GasUsage = pd.read_csv('GasUsage_complete.csv')

# Convert date to YYYY-MM-DD
GasUsage['Date'] = pd.to_datetime(GasUsage['Date'])
# Remove days with no gas usage
GasUsage = GasUsage[GasUsage['Gas']>0]




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
    deg = st.selectbox(
        "Degree of polynomial regression",
        [
            "1 (Linear)",
            "2 (Quadratic)",
            "3 (Cubic)",
            "4 (Quintic)",
        ]
    )


with col2:
    fig, ax = plt.subplots()

    #Take the first character of deg and cast it to an integer
    ord = int(deg[0])

    # Scatterplot of gas usage by temperature with degree 3 polynomial model
    sns.regplot(data=GasUsage, x='Average', y='Gas',
                    ci=False, line_kws={'color': 'black'}, order=ord)
    ax.set_xlabel('Temperature', fontsize=14)
    ax.set_ylabel('Gas', fontsize=14)
    st.pyplot(fig)
