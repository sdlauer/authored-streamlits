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
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """

st.markdown(hide, unsafe_allow_html=True)

crabs = pd.read_csv("crab-groups.csv")

crabs.columns = ["Site", "Latitude", "Sample size", "Mean length", "Min length", "Max length", "Stdev length","Median length","Date"]
crabs = crabs[["Site", "Date", "Sample size","Latitude","Mean length", "Min length", "Max length","Median length"]]
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


tab1, tab2, tab3, tab4 = st.tabs(["Plot", "Data","Prediction", "Summary statistics"])

with tab1:
    col1, col2 = st.columns([1.5,3])

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
        X = crabs[['Latitude']].values.reshape(-1, 1).astype(float)
        y = crabs[[target]].values.reshape(-1, 1).astype(float)

        # Logistic regression predicting diagnosis from tumor radius
        linearModel = LinearRegression()
        linearModel.fit(X,np.ravel(y.astype(int)))

        # regModeleq = st.checkbox("Display regression equation")
        add_reg = st.checkbox("Add regression line")
        add_mean = st.checkbox("Add mean")
        add_resid = st.checkbox("Add residuals")

        m, b = np.polyfit(np.ravel(X).astype(float), np.ravel(y).astype(float), 1)
        m = np.round(m,3)
        b = np.round(b,3)


    with col2:


        fig, ax = plt.subplots()
        sns.scatterplot(x="Latitude", y=target, data=crabs)
        ax.set_xlabel("Latitude", fontsize=14)
        ax.set_ylabel(target, fontsize=14)

        if add_reg:
            x_ind = [X.min(),X.max()]
            y_ind = [m*x_ind[0]+b, m*x_ind[1]+b]
            plt.plot(x_ind,y_ind, c='red', label="Regression line")
            plt.legend()

        if add_mean:
            x_ind = [X.min(),X.max()]
            y_mean = [crabs[target].mean(), crabs[target].mean()]
            plt.plot(x_ind,y_mean, c='darkorange', label="Mean")
            plt.legend()

        if add_resid:
            n = len(X)
            for i in range(len(X)):
                plt.plot([X[i],X[i]],[y[i],m*X[i]+b],color='grey',linewidth = 2)
        st.subheader("Plot")
        if add_reg: st.latex("\widehat{\\text{" + target + "}} = " + str(m) + "(\\text{Latitude})" + str(b))
        if add_mean: st.latex("\overline{\\text{" + target + "}} = " + str(np.round(crabs[target].mean(),2)))
        st.pyplot(fig)
        thisdict = {
          "Mean length": "mean fiddler crab length",
          "Min length": "minimum fiddler crab length",
          "Max length": "maximum fiddler crab length",
          "Median length": "median fiddler crab length"
        }
        desc1 = "Description: Samples of fiddler crabs from 13 locations were taken and the " + thisdict[target]
        desc2 = " from each location was recorded. As the latitude increases, the " + thisdict[target]
        desc3 = " also increases."
        description = desc1 + desc2 + desc3
        st.write(description)

with tab2:
    st.table(crabs)

with tab3:
    st.subheader("Regression equation")
    st.latex("\widehat{\\text{" + target + "}} = " + str(m) + "(\\text{Latitude})" + str(b))
    st.subheader("Prediction")
    pred_text = "Move slider to find the predicted " + thisdict[target] + " when Latitude is"
    predictor = st.slider(pred_text,30.0, 43.0, 30.0, 0.1)
    prediction = np.round(m*predictor+b,2)
    st.latex("\widehat{\\text{" + target + "}} (" + str(predictor) + ") = " + str(m) + "(" + str(predictor) + ")" + str(b) + " = " + str(prediction))

with tab4:
    st.subheader("Summary statistics")
    st.dataframe(crabs[["Latitude",target]].describe().T)
    st.subheader("Sum of squared errors")
    yPredicted = linearModel.predict(X)
    SSEreg = sum((y - yPredicted)**2)[0]
    SSEyBar = sum((y - np.mean(crabs[target]))**2)[0]
    ss_desc1 = "The sum of squared errors for the mean of the " + thisdict[target] + " is " + str(SSEyBar) + "."
    ss_desc2 = "The sum of squared errors for the least squares regression line is " + str(SSEreg) + "."
    ss_desc = ss_desc1 + ss_desc2
    st.write(ss_desc)
    st.subheader("Correlation coefficient")
