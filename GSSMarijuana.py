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


marijuana = pd.read_csv('gss.csv').dropna()

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

marijuana = pd.read_csv('https://raw.githubusercontent.com/zyRissler/streamlits/main/gss.csv').dropna()

seed=123

# Define input and output features
X = marijuana[['age', 'educ', 'polviews_num']]
y = marijuana[['marijuana01']]

col1, col2 = st.columns([2,1])

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
    classtreeModel = DecisionTreeClassifier(max_depth=depth, random_state=seed)

    # Fit the model
    classtreeModel = classtreeModel.fit(X,y)



#Plot the confusion matrix
with col2:
    if conf_mat:
        st.header("Confusion matrix")
        y_pred = classtreeModel.predict(X)
        if text:
            st.write(metrics.confusion_matrix(y, y_pred))
        else:
            disp = metrics.ConfusionMatrixDisplay.from_predictions(y, y_pred)
            #fig, ax = plt.subplots(figsize=(4,2))
            #disp.plot(ax=ax)
            st.pyplot(disp.figure_)

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
