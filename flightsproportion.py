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

#flights = pd.read_csv('flightsProp.csv')
#flights.columns = ["origin", "delay"]

#EWRf = flights[flights['origin']=='EWR']
#JFKf = flights[flights['origin']=='JFK']
#LGAf = flights[flights['origin']=='LGA']

flighttab = pd.DataFrame( data = [['All', 33170, 39564, 72734], 
    ['JFK', 8456, 10756, 19212], 
    ['LGA', 9793, 15385, 25178], 
    ['EWR', 59300, 61535, 28344]],
    columns = ['Origin', 'Delay', 'No delay', 'Total'],
    index=None)

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
    alternative = st.selectbox(
        "Alternative hypothesis",
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
            #counts = flights['delay'].value_counts()
            #summary = pd.DataFrame(data={'Origin': ['All'], 'No Delay': [counts[0]],'Delay': [counts[1]]})
            summary = flighttab[flighttab['Origin']=='All']
        elif group1 != "none" and group2 == "none":
              if group1 == "EWR":
                #counts = EWRf['delay'].value_counts()
                summary = flighttab[flighttab['Origin']=='EWR']
              elif group1 == "JFK":
                #counts = JFKf['delay'].value_counts()
                summary = flighttab[flighttab['Origin']=='JFK']
              else:
                #counts = LGAf['delay'].value_counts()
                summary = flighttab[flighttab['Origin']=='LGA']
              #summary = pd.DataFrame(data={'Origin': [group1], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        elif group1 == "none" and group2 != "none":
              if group2 == "EWR":
                #counts = EWRf['delay'].value_counts()
                summary = flighttab[flighttab['Origin']=='EWR']
              elif group2 == "JFK":
                #counts = JFKf['delay'].value_counts()
                summary = flighttab[flighttab['Origin']=='JFK']
              else:
                #counts = LGAf['delay'].value_counts()
                summary = flighttab[flighttab['Origin']=='LGA']
              #summary = pd.DataFrame(data={'Origin': [group2], 'No Delay': [counts[0]],'Delay': [counts[1]]})
        else:
         if group1 == "EWR":
            #counts1 = EWRf['delay'].value_counts()
            summary1 = flighttab[flighttab['Origin']=='EWR']
         elif group1 == "JFK":
            #counts1 = JFKf['delay'].value_counts()
            summary1 = flighttab[flighttab['Origin']=='JFK']
         else:
            #counts1 = LGAf['delay'].value_counts()
            summary1 = flighttab[flighttab['Origin']=='LGA']

         if group2 == "EWR":
            #counts2 = EWRf['delay'].value_counts()
            summary2 = flighttab[flighttab['Origin']=='EWR']
         elif group2 == "JFK":
            #counts2 = JFKf['delay'].value_counts()
            summary2 = flighttab[flighttab['Origin']=='JFK']
         else:
            #counts2 = LGAf['delay'].value_counts()
            summary2 = flighttab[flighttab['Origin']=='LGA']
         summary = pd.concat([summary1, summary2])
        st.dataframe(summary)

with col2:
    fig, (ax1, ax2) = plt.subplots(norws=1, ncols=2)
    if group1 == "none" and group2 == "none":
        ax1.bar(x=['Delay', 'No delay'], height=flighttab[flighttab['Origin']=='All'][['Delay', 'No delay']])
        ax2.set_visible(False)
    elif group1 != "none" and group2 = "none":
        ax1.bar(x=['Delay', 'No delay'], height=flighttab[flighttab['Origin']==group1][['Delay', 'No delay']])
        ax2.set_visible(False)
    elif group1 == "none" and group2 != "none":
        ax2.bar(x=['Delay', 'No delay'], height=flighttab[flighttab['Origin']==group2][['Delay', 'No delay']])
        ax1.set_visible(False)
    else:
        ax1.bar(x=['Delay', 'No delay'], height=flighttab[flighttab['Origin']==group1][['Delay', 'No delay']])    
        ax2.bar(x=['Delay', 'No delay'], height=flighttab[flighttab['Origin']==group2][['Delay', 'No delay']])
    st.pyplot(fig)







