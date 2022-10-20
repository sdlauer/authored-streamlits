import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#from statsmodels.stats.proportion import proportions_ztest

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

EWRf = flights[flights['origin']=='EWR']
JFKf = flights[flights['origin']=='JFK']
LGAf = flights[flights['origin']=='LGA']



col1, col2 = st.columns([2,3])

with col1:

    group1 = st.selectbox(
        "Group 1",
        [
            "none",
            "EWR",
            "JFK",
            "LGA"
        ]
    )

    group2 = st.selectbox(
        "Group 2",
        [
            "none",
            "EWR",
            "JFK",
            "LGA"
        ]
    )
    st.text("Null Hypothesis:")
    st.latex(r'''H_0: \pi_1 = \pi_2''')
    st.text("Alternative Hypothesis:")
    alternative = st.selectbox(
        "",
        [
            "not equal",
            "less than",
            "greater than",
        ]
    )
    if alternative == "not equal":
        st.latex(r'''H_a: \pi_1 \neq \pi_2''')
    elif alternative == "less than":
        st.latex(r'''H_a: \pi_1 \lt \pi_2''')
    else:
        st.latex(r'''H_a: \pi_1 \gt \pi_2''')

    check = st.checkbox("Display summary statistics")

    if check:
        if group1 == "none" and group2 == "none":
            counts = flights['delay'].value_counts()
            summary = pd.DataFrame(data={'Origin': ['All'], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        elif group1 != "none" and group2 == "none":
              if group1 == "EWR":
                counts = EWRf['delay'].value_counts()
              elif group1 == "JFK":
                counts = JFKf['delay'].value_counts()
              else:
                counts = LGAf['delay'].value_counts()
              summary = pd.DataFrame(data={'Origin': [group1], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        elif group1 == "none" and group2 != "none":
              if group2 == "EWR":
                counts = EWRf['delay'].value_counts()
              elif group2 == "JFK":
                counts = JFKf['delay'].value_counts()
              else:
                counts = LGAf['delay'].value_counts()
              summary = pd.DataFrame(data={'Origin': [group2], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        else:
         if group1 == "EWR":
            counts1 = EWRf['delay'].value_counts()
         elif group1 == "JFK":
            counts1 = JFKf['delay'].value_counts()
         else:
            counts1 = LGAf['delay'].value_counts()

         if group2 == "EWR":
            counts2 = EWRf['delay'].value_counts()
         elif group2 == "JFK":
            counts2 = JFKf['delay'].value_counts()
         else:
            counts2 = LGAf['delay'].value_counts()
         summary = pd.DataFrame(data={'Origin': [group1, group2], 
                'No Delay': [counts1[0], counts2[0]],'Delay': [counts1[1], counts2[1]]})
        st.dataframe(summary)

with col2:
    print('...in progress...')