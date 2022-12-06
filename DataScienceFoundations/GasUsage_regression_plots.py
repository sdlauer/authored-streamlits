import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Import and view the dataset
GasUsage = pd.read_csv('GasUsage_complete.csv')

# Convert date to YYYY-MM-DD
GasUsage['Date'] = pd.to_datetime(GasUsage['Date'])
# Remove days with no gas usage
GasUsage = GasUsage[GasUsage['Gas']>0]




hide = """
        <style>
        max-width: {max_width:400}px;
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {overflow: hidden;}
        div.block-container {padding-top:1rem;}
        div.block-container {padding-bottom:1rem;}
        </style>
        """

st.markdown(hide, unsafe_allow_html=True)


deg = st.selectbox(
    "Degree of polynomial regression",
    [
        "1 (Linear)",
        "2 (Quadratic)",
        "3 (Cubic)",
        "4 (Quartic)",
    ]
)

#I couldn't get the resizing to work to my satisfaction, so I used columns as a hackey way to keep the graph small and centered.
col1, col2, col3 = st.columns([1,3,1])

with col2:
    fig, ax = plt.subplots()

    #Take the first character of deg and cast it to an integer
    ord = int(deg[0])

    # Scatterplot of gas usage by temperature with polynomial model
    sns.regplot(data=GasUsage, x='Average', y='Gas',
        ci=False, line_kws={'color': 'black'}, order=ord)
    ax.set_xlabel('Temperature', fontsize=14)
    ax.set_ylabel('Gas', fontsize=14)
    st.pyplot(fig)

st.write("Description: A scatter plot of temperature and natural gas with a regression model of the chosen degree. The polynomial models with degree 2 and degree 3 appear to be good fits for the dataset. The polynomial model with degree 4 curves upward at the right end, suggesting that gas use will increase for high temperatures.")
