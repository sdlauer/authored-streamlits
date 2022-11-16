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

@st.cache
def loadData():
    # Read data, clean up names

    beans = pd.read_csv("Dry_Bean_Dataset.csv")
    beans['Class'] = beans['Class'].str.capitalize()
#    beans = beans.sample(750, random_state = 20221116)
    return beans

@st.cache
def labelMaker(y):
    # create a label encoder so colors match between plots
    le = preprocessing.LabelEncoder()
    le.fit(y)
    return le


@st.cache
def plot_classification_regions(X, y, classifier, le, with_data = False):

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
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    #Get outputs ready for plotting
    Z = le.transform(Z)
    Z = Z.reshape(xx.shape)
    numClasses = len(le.classes_)
    #Plot the regions classified as different beans
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, levels = [i-0.5 for i in range(numClasses+1)],
                 cmap = ListedColormap(sns.color_palette("colorblind", as_cmap = False, n_colors = numClasses)))

    if with_data:
        p1 = sns.scatterplot(data = X, x = X.columns[0], y  = X.columns[1],
                             hue = le.transform(np.ravel(y)), palette = "colorblind",
                    alpha = 1, edgecolor = "black",style = le.transform(np.ravel(y)),)
        leg = p1.legend()
        leg.set_title("Variety")
        for t, l in zip(leg.texts, le.inverse_transform(range(7))):
            t.set_text(l)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state = 20221116)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

col1, col2 = st.columns([3,2])

beanKnnClassifier = KNeighborsClassifier(n_neighbors = nbrs )
beanKnnClassifier.fit(X_train_scaled, np.ravel(y_train))
y_pred = beanKnnClassifier.predict(scaler.transform(X_test))

with col1:
    nbrs = st.slider(
        "k",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
    )

    accuracy = metrics.accuracy_score(y_pred, y_test)
    st.write(f"Accuracy: {accuracy:.3f}")

with col2:
    beanSample = beans.sample(750, random_state = 20220509)
    X = beanSample[["MajorAxisLength", "MinorAxisLength"]]
    y = beanSample[["Class"]]
    le = labelMaker(y)
    fig = plt.figure(figsize=(8,6))
    plot_classification_regions(X, y, beanKnnClassifier, le,
                                with_data = False)
    st.pyplot(fig)
