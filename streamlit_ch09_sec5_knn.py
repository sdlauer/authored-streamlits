import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score
from mlxtend.plotting import plot_decision_regions


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

@st.cache
def loadData():
        url = "https://raw.githubusercontent.com/aimeeschwab-mccoy/streamlit_asm/main/WisconsinBreastCancerDatabase.csv"

        cancer = pd.read_csv(url)
        cancer.columns = list(cancer.columns)

        cancer = cancer.replace(to_replace = ['M','B'],value = [int(1), int(0)])
        return cancer

cancer = loadData()

X = cancer[['Radius mean', 'Texture mean']]
y = cancer[['Diagnosis']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

images = {3: "knn_images/KNeigh3.png", 5: "knn_images/KNeigh5.png", 
                7: "knn_images/KNeigh7.png", 9: "knn_images/KNeigh9.png", 
                11: "knn_images/KNeigh11.png", 13: "knn_images/KNeigh13.png", 
                15: "knn_images/KNeigh15.png", 17: "knn_images/KNeigh17.png", 
                19: "knn_images/KNeigh19.png"}


col1, col2 = st.columns([1,3])

with col1:

        k = st.selectbox(
            "Select k",
            [3, 5, 7, 9, 11, 13, 15, 17, 19]
        )

        knn = KNeighborsClassifier(n_neighbors=k) 
        knn.fit(X_train_scaled, np.ravel(y_train))

        y_pred = knn.predict(X_train_scaled)
        accuracy = accuracy_score(y_train, y_pred)
        precision = precision_score(y_train, y_pred)
        recall = recall_score(y_train, y_pred)

        st.write("Performance metrics on training data")

        st.write("Accuracy = ", round(accuracy, 4))
        st.write("Precision = ", round(precision, 4))
        st.write("Recall =", round(recall, 4))

        #st.metric("Accuracy", round(accuracy, 4))
        #st.metric("Precision", round(precision, 4))
        #st.metric("Recall", round(recall, 4))


        
with col2:

        #fig, ax = plt.subplots()

        #print(y_train)

        #p = plot_decision_regions(X_train_scaled, np.ravel(y_train), clf=knn)
        #p.set_title('Training region: k-nearest neighbors, k=%i' %k)

        #st.pyplot(fig)

        st.image(images[k])

text_hider = st.checkbox('Hide description')

if text_hider:
        st.caption("")

else:
        st.caption("Description: Decision boundary for k-nearest neighbors model to predict cell type based on standardized radius mean and texture mean. Horiztonal and vertical axes range from -3 to +5. All models predict cells with higher radius and texture are malignant. Decision boundary for k=3 is not smooth. Decision boundary for k=7 is somewhat smooth. Decision boundary for  k=11 is mostly smooth.")



