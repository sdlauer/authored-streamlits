"""
Created on Wed Nov 16 10:50:17 2022

@author: mrissler
"""

import streamlit as st
#import needed packages for classification
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd   #### not needed ####
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
# from mlxtend.plotting import plot_decision_regions

@st.cache
def loadData():
    # Read data, clean up names
    beans = pd.read_csv("Dry_Bean_Dataset.csv")
    beans['Class'] = beans['Class'].str.capitalize()
    beans = beans.sample(1000, random_state=20221116)
    return beans

@st.cache
def labelMaker(y):
    # create a label encoder so colors match between plots
    le = preprocessing.LabelEncoder()
    le.fit(y)
    return le

@st.cache
def doSplitAndScale(beans):
        X = beans[["MajorAxisLength", "MinorAxisLength"]]
        y = beans[["Class"]]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                            random_state=20221116)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        le = labelMaker(y)

        return X_train, X_test, y_train, y_test, scaler, X_train_scaled, X_test_scaled, le

# @st.cache
def plot_classification_regions(X, y, classifier, scaler, le, nbrs, with_data=False):  #######################

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
    plt.rc('axes', labelsize=16)
    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)
    plt.rc('legend', fontsize=14)
    #Plot the regions classified as different beans
    fig, ax = plt.subplots(figsize=(8,6))
    plt.contourf(xx, yy, Z, levels=[i-0.5 for i in range(numClasses+1)],
                cmap=ListedColormap(sns.color_palette("colorblind",
                as_cmap=False, n_colors=numClasses)), alpha = 0.75)
    plt.xlabel("Major axis length")
    plt.ylabel("Minor axis length")

    if with_data:
        p1 = sns.scatterplot(data=X, x=X.columns[0], y=X.columns[1],
                hue=le.transform(np.ravel(y)), palette="colorblind",
                alpha=1, edgecolor="black",style=le.transform(np.ravel(y)),)
        leg = p1.legend()
        leg.set_title("Variety",prop={'size':16})
        for t, l in zip(leg.texts, le.inverse_transform(range(7))):
            t.set_text(l)
    plt.savefig("imagesKnnBeans/kNNBeans" + str(nbrs) + str(with_data) + ".png") ################ used to save images ##########
    return fig, ax

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

beans = loadData() #### not needed ####
X_train, X_test, y_train, y_test, scaler, X_train_scaled, X_test_scaled, le = doSplitAndScale(beans)  #### not needed ##############
#accrcyTrainDict = {1 : 0.8333, 3 : 0.85, 5 : 0.8367, 7 : 0.8367, 9 : 0.8533, 11:  0.8467, 13:  0.8567, 15:  0.8567, 17:  0.8567, 19:  0.8567, 21:  0.86} 
#accrcyTestDict = {1 : 0.8333, 3 : 0.85, 5 : 0.8367, 7 : 0.8367, 9 : 0.8533, 11:  0.8467, 13:  0.8567, 15:  0.8567, 17:  0.8567, 19:  0.8567, 21:  0.86} 
col1, col2 = st.columns([2,4])
with col1:
    nbrs = st.slider(
        "k",
        min_value=1,
        max_value=21,
        value=11,
        step=2,
    )

    beanKnnClassifier = KNeighborsClassifier(n_neighbors=nbrs )
    beanKnnClassifier.fit(X_train_scaled, np.ravel(y_train))
    
    y_pred = beanKnnClassifier.predict(X_test_scaled)
    accuracyTest = metrics.accuracy_score(y_test, y_pred)

    y_pred = beanKnnClassifier.predict(X_train_scaled)
    accuracyTrain = metrics.accuracy_score(y_train, y_pred)
    # precision = metrics.precision_score(y_test, y_pred)
    # recall = metrics.recall_score(y_test, y_pred)

    st.write("Accuracy on training set=", round(accuracyTrain,4))
    st.write("Accuracy on test set=", round(accuracyTest,4))
    #st.write("Accuracy on test set=", accrcydict[nbrs])
    print(nbrs, round(accuracyTrain,4))  ######### used to make accrcydict ####################
    print(nbrs, round(accuracyTest,4))  ######### used to make accrcydict ####################
    # st.write("Precision = ", round(precision, 4))
    # st.write("Recall =", round(recall, 4))

    # st.write(metrics.confusion_matrix(y_test, y_pred))

    hidePts = st.checkbox("Hide training data")

    textOption = st.checkbox("Text description")


with col2:
    #beanSample = beans.sample(750, random_state=20220509)
    #X = beanSample[["MajorAxisLength", "MinorAxisLength"]]
    #y = beanSample[["Class"]]
    if not textOption:
        fig, ax = plot_classification_regions(X_train, y_train,
                                                beanKnnClassifier, scaler, le,
                                                nbrs, with_data=not hidePts) ############ needed nbrs attr, then don't need fig and ax ##########
        st.pyplot(fig)   ################## don't generate plots  #####################
        #st.image("imagesKnnBeans/kNNBeans" + str(nbrs) + str(not hidePts)+ ".png") ############## show images ###############
    else:
        st.markdown('''The plot has MajorAxisLength on the horizontal axis and varies
                      between 190 and 730 and has MinorAxisLength on the vertical axis
                      and varies between 135 to 420.''')
        if not hidePts:
            st.markdown('''The points are mostly clustered along the diagonal
                  from the lower left corner (190,135) to the upper right corner (420, 730).
                  Dermason beans are in the lower left hand corner, being the smallest
                  in both dimensions. Seker beans have slightly longer major axis length
                  than Dermason, but a much longer minor axis length. Sira beans have a
                  similar minor axis length to Seker beans, but a longer major axis length
                  than both Dermason and Seker beans. Horoz beans have a similar minor axis
                  length to Sira beans (and some overlap with Dermason), but a longer major
                  axis length than all the beans described so far. Barbunya beans have a
                  major axis length that overlaps with Sira and Dermason but longer major
                  axis length than both.  Cali beans have a similar minor axis length
                  to Barbunya beans, but a longer major axis length. Bombay beans are the
                  largest beans in both dimensions and occupy the upper right corner of the
                  plot.''')

        st.markdown('''For k=11 points are classified as:

* Dermason beans - within a region that is roughly a quadrilateral with vertices
    (190, 135), (310, 135), (290, 175), and (190, 175)

* Seker beans - within a roughly triangular region with
        vertices (190, 175), (300, 210), and (190, 310)

* Sira beans - within a roughly quadrilateral region with
        vertices (290,175), (300, 160), (350, 190), and (300, 210)

* Horoz beans - within a roughly pentagonal region with
        vertices (310, 135), (730, 135), (730, 150), (350, 190), and (300, 160)

* Barbunya beans - within a roughly hexagonal region with
        vertices (190, 310), (300, 210), (390, 210), (420, 330), (250, 420), and
        (190, 420)

* Cali beans - within a roughly quadrilateral with vertices
        (390, 210), (730, 150), (730, 250), and (430, 320)

* Bombay beans - above the line between (250, 420) and (730, 250)

The boundaries near the diagonal for the regions vary some with k, but the center of each region does not change for different values of k.
''')