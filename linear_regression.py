import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

crabs = pd.read_csv("crab-groups.csv")

crabs.columns = ["Site", "Latitude", "Sample size", "Mean length", "Min length", "Max length", "Stdev length","Median length","Date"]

# # Show linear regression equation
# def show_eq(X,y,target):
#     m, b = np.polyfit(X, y, 1)
#     m = round(m,3)
#     b = round(b,3)
#     st.latex('\hat{\text{' + target + '}} = ' + str(m) + '(\text{Latitude}) + ' + str(b))
#
# # Plot linear regression line
# def add_reg(data):
#     m, b = np.polyfit(data[0], data[1], 1)
#     x = [1,100]
#     y = [m*x[0]+b, m*x[1]+b]
#     plt.plot(x,y, c='red')
#
# # Add residuals to the plot
# def add_resid(data):
#     n = len(data[0])
#     m, b = np.polyfit(data[0], data[1], 1)
#     y_pred = m*data[0] + b
#     for i in range(n):
#         plt.plot([data[0][i],data[0][i]],[data[1][i],y_pred[i]], c = 'black')
#
# # Show linear regression equation
# def show_eq(data):
#     m, b = np.polyfit(data[0], data[1], 1)
#     m = round(m,3)
#     b = round(b,3)
#     plt.text(110,0,'y =' + str(m) + 'x + ' + str(b))
#
# # Show correlation coefficient
# def show_corr(data):
#     # Note: np.corrcoef gives a correlation matrix
#     corr_coef = np.corrcoef(data[0],data[1])
#     corr_coef = round(corr_coef[0,1],3)
#     plt.text(110,2,'r = ' + str(corr_coef))


col1, col2 = st.columns([1,3])

with col1:
    target = st.selectbox(
        "Select target feature",
        [
            "Mean length",
            "Min length",
            "Max length",
            "Median length"
        ]
    )

    # Store relevant columns as variables
    X = crabs[['Latitude']].values.reshape(-1, 1).astype(int)
    y = crabs[[target]].values.reshape(-1, 1).astype(int)

    # Logistic regression predicting diagnosis from tumor radius
    linearModel = LinearRegression()
    linearModel.fit(X,np.ravel(y.astype(int)))

    regModeleq = st.checkbox("Display regression model")
    add_reg = st.checkbox("Add Rrgression line")
    regModelmean = st.checkbox("Show mean of " + str(target))

m, b = np.polyfit(np.ravel(X).astype(int), np.ravel(y).astype(int), 1)
m = np.round(m,3)
b = np.round(b,3)

with col2:
    fig, ax = plt.subplots()
    sns.scatterplot(x="Latitude", y=target, data=crabs)
    ax.set_xlabel("Latitude", fontsize=14)
    ax.set_ylabel(target, fontsize=14)

    if regModeleq:
        st.latex("\widehat{\\text{" + target + "}} = " + str(m) + "(\\text{Latitude})" + str(b))

    if add_reg:
        x_ind = [1,100]
        y_pred = [m*x[0]+b, m*x[1]+b]
        plt.plot(x_ind,y_pred, c='red')
    # regModeleq = st.checkbox("Display regression model")
    # if regModeleq: show_eq(X,y,target)

    st.pyplot(fig)
