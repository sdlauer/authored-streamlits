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

col1, col2 = st.columns([2,3])

with col1:

#Set depth
    depth = st.slider(
        "Depth of tree",
        min_value=1,
        max_value=4,
        value=2,
        step=1,
        )

    text = st.checkbox('Text output')

    # Initialize the model
    classtreeModel = DecisionTreeClassifier(max_depth=depth, random_state=seed)

    # Fit the model
    classtreeModel = classtreeModel.fit(X,y)



#Plot the confusion matrix
with col2:
    st.header("Confusion matrix")
    y_pred = classtreeModel.predict(X)
    if text:

        st.write(metrics.confusion_matrix(y, y_pred))
    else:
        disp = metrics.ConfusionMatrixDisplay.from_predictions(y, y_pred)

        st.pyplot(disp.figure_)

#Plot the tree
st.header("Classification tree")
if text:
    st.text(export_text(classtreeModel))
else:
    fig, ax = plt.subplots()
    plot_tree(classtreeModel, feature_names=X.columns,
                       filled=True, fontsize=None, )
    st.pyplot(fig)
