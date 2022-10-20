import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

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

flights = pd.read_csv('flightsProp.csv')
flights.columns = ["origin", "delay"]

EWR = flights[flights['origin']=='EWR']
JFK = flights[flights['origin']=='JFK']
LGA = flights[flights['origin']=='LGA']



col1, col2 = st.columns([2,3])

with col1:

    group1 = st.selectbox(
        "Group 1",
        [
            "none"
            "EWR",
            "JFK",
            "LGA"
        ]
    )

    group2 = st.selectbox(
        "Group 2",
        [
            "none"
            "EWR",
            "JFK",
            "LGA"
        ]
    )

    check = st.checkbox("Display summary statistics")

    if check:
        if group1 == "none" and group2 == "none":
            counts = flights['delay'].value_counts()
            summary = pd.DataFrame(data={'Origin': ['All'], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        elif group1 != "none" and group2 == "none":
              counts = group1['delay'].value_counts()
              summary = pd.DataFrame(data={'Origin': [group1], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        elif group1 == "none" and group2 != "none":
              summary = group2['delay'].value_counts()
              summary = pd.DataFrame(data={'Origin': [group2], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        else:
         counts1 = counts = group1['delay'].value_counts()
         counts2 = counts = group2['delay'].value_counts()
         summary = pd.DataFrame(data={'Origin': [group1, group2], 
                'No Delay': [counts1[0], counts2[0]],'Delay': [counts1[1], counts2[1]]})
        st.dataframe(summary)

with col2:
