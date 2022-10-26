import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


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

url = "https://raw.githubusercontent.com/aimeeschwab-mccoy/streamlit_asm/main/tripadvisor_review.csv"

reviews = pd.read_csv(url)
reviews.columns = list(reviews.columns)

X = reviews.drop(axis=1, labels=['User ID'])
kmModel = KMeans(n_clusters = 4, random_state=123)
kmModel = kmModel.fit(X)
clusters = kmModel.fit_predict(X)
centroids = kmModel.cluster_centers_



col1, col2 = st.columns([2,3])

with col1:

    destination = st.selectbox(
        "Select destination type",
        [
            "Art", "Clubs", "Juice bars", "Restaurants", "Museums", "Resorts",
            "Parks", "Beaches", "Theaters", "Religious"
        ]
    )

    check = st.checkbox("Display descriptive statistics")

    if check:
        summary = X[[destination]].groupby(clusters).describe().round(2)
        st.dataframe(summary)

with col2:
    fig, ax = plt.subplots()

    p = sns.kdeplot(data=X, x=destination, hue=clusters, palette="viridis", linewidth=2.5)
    p.set_ylabel("Density", fontsize=14)
    p.set_xlabel(destination, fontsize=14)
    p.set_title("Travel ratings by cluster", fontsize=16)


    st.pyplot(fig)