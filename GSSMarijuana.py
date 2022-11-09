# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:50:17 2022

@author: mrissler
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn import metrics, tree


@st.cache
def loadData():
    df = pd.read_csv('gss.csv').dropna()
    return df

marijuana = loadData()

@st.cache
def fitModel(depth, seed):
    # Initialize the model
    model = DecisionTreeClassifier(max_depth=depth, random_state=seed)

    # Fit the model
    model = model.fit(X,y)
    return model

@st.cache
def getPred(model, X)
    predictions = model.predict(X)
    return predictions

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


seed=123

# Define input and output features
X = marijuana[['age', 'educ', 'polviews_num']]
y = marijuana[['marijuana01']]

col1, col2 = st.columns([3,2])

with col1:
    st.header("Inputs")
#Set depth
    depth = st.slider(
        "Depth of tree",
        min_value=1,
        max_value=3,
        value=3,
        step=1,
        )

    text = st.checkbox('Text output')
    conf_mat = st.checkbox('Display confusion matrix')

    # Initialize the model
    classtreeModel = fitModel(depth, seed)


#Plot the confusion matrix
with col2:
    if conf_mat:
        st.header("Confusion matrix")
        y_pred = getPred(classtreeModel, X)
        if text:
            st.write(metrics.confusion_matrix(y, y_pred))
        else:
            disp = metrics.ConfusionMatrixDisplay.from_predictions(y, y_pred)
            fig, ax = plt.subplots(figsize=(2,2))
            disp.plot(ax=ax)
            st.pyplot(fig)
            #st.pyplot(disp.figure_)


#Plot the tree
st.header("Classification tree")
if text:
    #st.text(X.columns)
    st.text(export_text(classtreeModel, feature_names=X.columns.to_list()))
else:
    #fig, ax = plt.subplots()


    fig = plt.figure(figsize=(pow(2,depth)*4,depth*3))
    if depth < 3:
        plot_tree(classtreeModel, feature_names=X.columns,
                  filled=True, fontsize=None, )

    else:
        plot_tree(classtreeModel, feature_names=X.columns,
                  filled=True, fontsize=25, )

    st.pyplot(fig)

    if depth > 2:
        st.text("Right-click to open image in a new tab for a larger view.")
