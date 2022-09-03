import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

mpg = pd.read_csv("mpg.csv")
mpg = mpg.astype({"horsepower":"int"})

st.title("Regression using the mpg dataset")

input_feat = st.selectbox(
    "Input feature",
    [
        "mpg",
        "displacement",
        "weight",
        "acceleration",
    ]
)

output_feat = st.selectbox(
    "Output feature",
    [
        "mpg",
        "displacement",
        "weight",
        "acceleration",
    ]
)

reg_line = st.checkbox("Regression line")
reg_eq = st.checkbox("Regression equation")
corr_coef = st.checkbox("Correlation coefficient")

# Plot linear regression line
def add_reg(data):
    m, b = np.polyfit(data[0], data[1], 1)
    x = [1,100]
    y = [m*x[0]+b, m*x[1]+b]
    plt.plot(x,y, c="red")

# Add residuals to the plot
def add_resid(data):
    n = len(data[0])
    m, b = np.polyfit(data[0], data[1], 1)
    y_pred = m*data[0] + b
    for i in range(n):
        plt.plot([data[0][i],data[0][i]],[data[1][i],y_pred[i]], c = "black")

# Show linear regression equation
def show_eq(data):
    m, b = np.polyfit(data[0], data[1], 1)
    m = round(m,3)
    b = round(b,3)
    plt.text(110,0,"y =" + str(m) + "x + " + str(b))

# Show correlation coefficient
def show_corr(data):
    # Note: np.corrcoef gives a correlation matrix
    corr_coef = np.corrcoef(data[0],data[1])
    corr_coef = round(corr_coef[0,1],3)
    plt.text(110,2,"r = " + str(corr_coef))

fig, ax = plt.subplots()
ax = sns.regplot(x=input_feat, y=output_feat, data=mpg, fit_reg=reg_line, line_kws={"color": "grey"})


# if reg_eq: show_eq(mpg[input_feat],mpg[output_feat])
# if corr_coef: show_corr(mpg[input_feat],mpg[output_feat])

st.pyplot(fig)
