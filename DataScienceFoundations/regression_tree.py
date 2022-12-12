# Import packages and functions
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn import tree, metrics


#@st.cache
def loadData():
    # Load the penguins data from palmerpenguins package
    penguins = sns.load_dataset('penguins')
    # Drop penguins with missing values
    penguins = penguins.dropna() 
    # Create a new data frame with only Gentoo penguins
    gentoo = penguins[penguins['species']=='Gentoo']

    # Create a matrix of input features with sex, flipper length, and bill length
    X = gentoo[['sex', 'flipper_length_mm', 'bill_length_mm']]
    # Use pd.get_dummies to convert sex to a binary (0/1) dummy variable
    X_dummies = pd.get_dummies(X, drop_first=True) 
    y = gentoo['body_mass_g']
    return X_dummies, y


seed = 123



X_dummies, y = loadData()

col1, col2 = st.columns([2,4])

with col1:
    treeDepth = st.slider(
        "Depth",
        min_value=1,
        max_value=5,
        value=2,
        step=1,
    )
    regtreeModel = DecisionTreeRegressor(max_depth=treeDepth, min_samples_leaf=2)
    regtreeModel.fit(X_dummies, y)
    plotFit = st.checkbox("Plot fitted data")

    textOption = st.checkbox("Text output")

with col2:
    X = X_dummies
    X['pred'] = regtreeModel.predict(X)

    if plotFit:
        fig = plt.figure(figsize=(6,6))
        p = sns.scatterplot(data=X, x='body_mass_g', 
                    y='pred', hue='sex')
        p.set_xlabel('Observed body mass', fontsize=14)
        p.set_ylabel('Predicted body mass', fontsize=14)
        st.pyplot(fig)

# Print tree
if textOption:
    st.text(export_text(regtreeModel, feature_names=X.columns.to_list()))
else:
    fig = plt.figure(figsize=(pow(2,treeDepth)*4, treeDepth*3))

    tree.plot_tree(regtreeModel, feature_names=X.columns, 
                       class_names=y.unique(), filled=False)

    st.pyplot(fig)

