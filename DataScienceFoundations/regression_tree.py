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
    return gentoo

def XySplit(df, output):
    X = df.copy()
    y = X.pop(output)
    # Use pd.get_dummies to convert sex to a binary (0/1) dummy variable
    X_dummies = pd.get_dummies(X, drop_first=True) 
    return X, X_dummies, y




seed = 123

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

#st.markdown(hide, unsafe_allow_html=True)

gentoo = loadData()

col1, col2 = st.columns([2,4])

with col1:
    st.header('Options')
    fitFeature = st.selectbox("Feature to predict", gentoo.select_dtypes(include='number').columns)

    X, X_dummies, y = XySplit(gentoo, fitFeature)

    treeDepth = st.slider(
        "Depth",
        min_value=1,
        max_value=4,
        value=2,
        step=1,
    )
    regtreeModel = DecisionTreeRegressor(max_depth=treeDepth, min_samples_leaf=2)
    regtreeModel.fit(X_dummies, y)
    plotFit = st.checkbox("Plot predictions")

    textOption = st.checkbox("Text output")
    
    X['pred'] = regtreeModel.predict(X_dummies)
    X['body_mass_g'] = y

    st.write("MSE = ", round(metrics.mean_squared_error(X['pred'], y), 1))

with col2:
    if plotFit:
        st.header('Predictions')
        if textOption:
            st.markdown('''The observed body mass is plotted on the horizontal axis and 
            the predicted body mass is plotted on the vertical axis. There are horizontal lines of points 
            that correspond to each leaf in the decision tree. The female penguins have lower predicted body mass 
            than the male penguins for all depths of trees.''')
        else:
            fig, ax = plt.subplots(figsize=(4,4))
            p = sns.scatterplot(data=X, x='body_mass_g', 
                                y='pred', hue='sex', style='sex')
            p.set_xlabel('Observed body mass', fontsize=14)
            p.set_ylabel('Predicted body mass', fontsize=14)
            ax.axline(xy1=(5000,5000), slope=1, color='b')
            st.pyplot(fig)

# Print tree
st.header("Regression tree")
if textOption:
    st.text(export_text(regtreeModel, feature_names=X_dummies.columns.to_list()))
else:
    fig = plt.figure(figsize=(pow(2,treeDepth)*4, treeDepth*3))

    tree.plot_tree(regtreeModel, feature_names=X_dummies.columns, 
                       class_names=y.unique(), filled=False, fontsize=15,
                       precision = 2)

    st.pyplot(fig)

    if treeDepth > 2:
        st.text("Right-click to open image in a new tab for a larger view.")