import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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

WBCD = pd.read_csv("WisconsinBreastCancerDatabase.csv")
WBCD.loc[WBCD['Diagnosis']=='B','Diagnosis']=0
WBCD.loc[WBCD['Diagnosis']=='M','Diagnosis']=1

# Store relevant columns as variables
X = WBCD[['Radius mean']].values.reshape(-1, 1)
y = WBCD[['Diagnosis']].values.reshape(-1, 1).astype(int)

col1, col2 = st.columns([1,3])

with col1:
    st.write("Threshold")
    # threshold=st.slider("Threshold", min_value=0, max_value=1, value=0.5, step=0.1)

with col2:
    #Logistic regression predicting diagnosis from tumor radius
    logisticModel = LogisticRegression()
    logisticModel.fit(X,np.ravel(y.astype(int)))

    #Graph logistic regression probabilities
    fig, ax = plt.subplots()
    plt.scatter(X,y)
    xDelta = np.linspace(X.min(),X.max(),10000)
    yPredicted = logisticModel.predict(X).reshape(-1,1).astype(int)
    yDeltaProb = logisticModel.predict_proba(xDelta.reshape(-1,1))[:,1]
    plt.plot(xDelta,yDeltaProb, color='red')
    ax.set_xlabel('Radius mean',fontsize=14);
    ax.set_ylabel('Probability tumor is malignant',fontsize=14);
    st.pyplot(fig)
