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

@st.cache
def loadData():
    url = "https://raw.githubusercontent.com/aimeeschwab-mccoy/streamlit_asm/main/ratings_clustered.csv"

    reviews = pd.read_csv(url)
    reviews.columns = list(reviews.columns)
    return reviews

reviews = loadData()

#X = reviews.drop(axis=1, labels=['User ID'])
#kmModel = KMeans(n_clusters = 4, random_state=123)
#kmModel = kmModel.fit(X)
#clusters = kmModel.fit_predict(X)
#centroids = kmModel.cluster_centers_

images = {"Art": "clustering_images/art.png", "Clubs": "clustering_images/clubs.png", 
            "Juice bars": "clustering_images/juice.png", "Restaurants": "clustering_images/restaurants.png", 
            "Museums": "clustering_images/museums.png", "Resorts": "clustering_images/resorts.png",
            "Parks": "clustering_images/parks.png", "Beaches": "clustering_images/beaches.png", 
            "Theaters": "clustering_images/theaters.png", "Religious sites": "clustering_images/religious.png"}

col1, col2 = st.columns([2,3])

with col1:

    destination = st.selectbox(
        "Select destination type",
        [
            "Art", "Clubs", "Juice bars", "Restaurants", "Museums", "Resorts",
            "Parks", "Beaches", "Theaters", "Religious sites"
        ]
    )

    check = st.checkbox("Display descriptive statistics")

    if check:
        summary = reviews[[destination, "clusters"]].groupby(by=["clusters"]).describe().round(2)
        st.dataframe(summary)

with col2:
    #fig, ax = plt.subplots()

    #p = sns.kdeplot(data=X, x=destination, hue=clusters, palette="viridis", linewidth=2.5)
    #p.set_ylabel("Density", fontsize=14)
    #p.set_xlabel(destination, fontsize=14)
    #p.set_title("Travel ratings by cluster", fontsize=16)

    #st.pyplot(fig)

    st.image(images[destination])

    text_hider = st.checkbox('Hide description')

    if text_hider:
        st.caption("")

    else:
        st.caption("Description: Density plots of travel ratings grouped by cluster membership.")