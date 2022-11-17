"""
Created on Wed Nov 16 10:50:17 2022

@author: mrissler
"""

import streamlit as st
#import needed packages for classification
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import packages for visualization of results
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib.colors import ListedColormap

#import packages for evaluation
from sklearn.model_selection import train_test_split
from sklearn import metrics
#from mlxtend.plotting import plot_decision_regions

@st.cache
def loadData():
    # Read data, clean up names

    beans = pd.read_csv("Dry_Bean_Dataset.csv")
    beans['Class'] = beans['Class'].str.capitalize()
    beans = beans.sample(1000, random_state = 20221116)
    return beans

@st.cache
def labelMaker(y):
    # create a label encoder so colors match between plots
    le = preprocessing.LabelEncoder()
    le.fit(y)
    return le

#@st.cache
def plot_classification_regions(X, y, classifier, scaler, le, with_data = False):

    #Define function for the plot.
    # X - two feature data frame,
    # y - output feature,
    # classifier - model that has been fit,
    # le - label encoder
    # with_data - plot the data with the regions

    #predict beans on a regular grid

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X.iloc[:,0].min() - 10, X.iloc[:,0].max() + 10
    y_min, y_max = X.iloc[:,1].min() - 10, X.iloc[:,1].max() + 10
    xh = (x_max - x_min)/200 # step size in the mesh for the x direction
    yh = (y_max - y_min)/200# step size in the mesh for the y direction

    xx, yy = np.meshgrid(np.arange(x_min, x_max, xh), np.arange(y_min, y_max, yh))
    Z = classifier.predict(scaler.transform(np.c_[xx.ravel(), yy.ravel()]))
    #Get outputs ready for plotting
    Z = le.transform(Z)
    Z = Z.reshape(xx.shape)
    numClasses = len(le.classes_)
    #Plot the regions classified as different beans
    fig, ax = plt.subplots(figsize=(8,6))
    plt.contourf(xx, yy, Z, levels = [i-0.5 for i in range(numClasses+1)],
                 cmap = ListedColormap(sns.color_palette("colorblind",
                 as_cmap = False, n_colors = numClasses)))

    if with_data:
        p1 = sns.scatterplot(data = X, x = X.columns[0], y  = X.columns[1],
                             hue = le.transform(np.ravel(y)), palette = "colorblind",
                    alpha = 1, edgecolor = "black",style = le.transform(np.ravel(y)),)
        leg = p1.legend()
        leg.set_title("Variety")
        for t, l in zip(leg.texts, le.inverse_transform(range(7))):
            t.set_text(l)
    return fig, ax

beans = loadData()

X = beans[["MajorAxisLength", "MinorAxisLength"]]
y = beans[["Class"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state = 20221116)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

col1, col2 = st.columns([2,4])



with col1:
    nbrs = st.slider(
        "k",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
    )

    beanKnnClassifier = KNeighborsClassifier(n_neighbors = nbrs )
    beanKnnClassifier.fit(X_train_scaled, np.ravel(y_train))
    y_pred = beanKnnClassifier.predict(scaler.transform(X_test))

    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)

    st.write("Accuracy =", round(accuracy,4))
    st.write("Precision = ", round(precision, 4))
    st.write("Recall =", round(recall, 4))

    showPts = st.checkbox("Show training data")


with col2:
    #beanSample = beans.sample(750, random_state = 20220509)
    #X = beanSample[["MajorAxisLength", "MinorAxisLength"]]
    #y = beanSample[["Class"]]
    le = labelMaker(y)

    fig, ax = plot_classification_regions(X_train, y_train, beanKnnClassifier, scaler, le,
                                with_data = showPts)
    st.pyplot(fig)
