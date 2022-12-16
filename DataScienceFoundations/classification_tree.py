# Import packages and functions
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import tree, metrics


def loadData():
    # Load the penguins data from palmerpenguins package
    penguins = sns.load_dataset('penguins')
    # Drop penguins with missing values
    penguins = penguins.dropna()
    return penguins


def XySplit(df, output):
    X = df.copy()
    y = X.pop(output)
    # Use pd.get_dummies to convert sex to a binary (0/1) dummy variable
    X_dummies = pd.get_dummies(X, drop_first=True)
    return X, X_dummies, y


@st.cache
def getPred(model, X):
    predictions = model.predict(X)
    return predictions


def do_stuff_on_page_load():
    st.set_page_config(layout="wide")
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


seed = 123

do_stuff_on_page_load()

gentoo = loadData()

col1, col2 = st.columns([2, 3])

with col1:
    st.header('Options')
    fitFeature = st.selectbox("Feature to predict",
                              gentoo.select_dtypes(include='object').columns)

    X, X_dummies, y = XySplit(gentoo, fitFeature)

    treeDepth = st.slider(
        "Depth",
        min_value=1,
        max_value=4,
        value=2,
        step=1,
    )
    clstreeModel = DecisionTreeClassifier(max_depth=treeDepth,
                                          min_samples_leaf=2)
    clstreeModel.fit(X_dummies, y)
    confMat = st.checkbox("Show confusion matrix")

    textOption = st.checkbox("Text output")


with col2:
    if confMat:
        st.header("Confusion matrix")
        y_pred = getPred(clstreeModel, X_dummies)
        if textOption:
            st.write(metrics.confusion_matrix(y, y_pred))
        else:
            disp = metrics.ConfusionMatrixDisplay.from_predictions(y, y_pred)
            fig, ax = plt.subplots(figsize=(4, 4))
            disp.plot(ax=ax)
            st.pyplot(fig)


# Print tree
st.header("Classification tree")
if textOption:
    st.text(export_text(clstreeModel,
                        feature_names=X_dummies.columns.to_list()))
else:
    fig = plt.figure(figsize=(pow(2, treeDepth)*4, treeDepth*3))

    tree.plot_tree(clstreeModel, feature_names=X_dummies.columns,
                   class_names=y.unique(), filled=False, fontsize=15,
                   precision=2, rounded=True)

    st.pyplot(fig)

    if treeDepth > 2:
        st.text("Right-click to open image in a new tab for a larger view.")
