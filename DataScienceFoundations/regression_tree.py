# Import packages and functions
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn import tree, metrics


@st.cache
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
    X_dummies

    y = gentoo['body_mass_g']
    return X_dummies, y


seed = 123



X_dummies, y = loadData()

col1, col2 = st.columns([2,4])

with col1:
    depth = st.slider(
        "Depth",
        min_value=1,
        max_value=5,
        value=2,
        step=1,
    )
    regtreeModel = DecisionTreeRegressor(max_depth=depth, min_samples_leaf=2, seed = seed)
    regtreeModel.fit(X_dummies, y)
    plotFit = st.checkbox("Plot fitted data")

    textOption = st.checkbox("Text output")

with col2:

    X_dummies['pred'] = regtreeModel.predict(X_dummies)

    if plotFit:
        p = sns.scatterplot(data=X_dummies, x='body_mass_g', 
                    y='pred', hue='sex')
        p.set_xlabel('Observed body mass', fontsize=14)
        p.set_ylabel('Predicted body mass', fontsize=14)

# Print tree
if textOption:
    st.text(export_text(regtreeModel, feature_names=X_dummies.columns.to_list()))
else:
    plt.figure(figsize = [12,8])

    p = tree.plot_tree(regtreeModel, feature_names=X_dummies.columns, 
                       class_names=y.unique(), filled=False, fontsize=10)

    st.pyplot(p)

