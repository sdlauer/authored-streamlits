import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

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

flights = pd.read_csv('flightsmean.csv')
flights.columns = ["origin", "dep_delay", "arr_delay"]

EWRf = flights[flights['origin']=='EWR']
JFKf = flights[flights['origin']=='JFK']
LGAf = flights[flights['origin']=='LGA']

col1, col2 = st.columns([2,3])

with col1:

	numerical  =st.selectbox(
		"Numerical feature",
		[
			"Departure delay",
			"Arrival delay"
		]
	)
	
	if numerical == "Departure delay":
		nf="dep_delay"
	else:
		nf="arr_delay"

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
    st.latex(r'''H_0: \mu_1 = \mu_2''')
    alternative = st.selectbox(
        "Alternative hypothesis",
        [
            "not equal",
            "less than",
            "greater than",
        ]
    )
    if alternative == "not equal":
        st.latex(r'''H_a: \mu_1 \neq \mu_2''')
    elif alternative == "less than":
        st.latex(r'''H_a: \mu_1 \lt \mu_2''')
    else:
        st.latex(r'''H_a: \mu_1 \gt \mu_2''')

    check = st.checkbox("Display summary statistics")

    if check:
        if group1 == "none" and group2 == "none":
            summary = flights[nf].describe()
        elif group1 != "none" and group2 == "none":
              if group1 == "EWR":
                summary = ERWf[nf].describe()
              elif group1 == "JFK":
                summary = JFKf[nf].describe()
              else:
                summary = LGAf[nf].describe()
        elif group1 == "none" and group2 != "none":
              if group2 == "EWR":
                summary = ERWf[nf].describe()
              elif group2 == "JFK":
                summary = JFKf[nf].describe()
              else:
                summary = LGAf[nf].describe()
        else:
         if group1 == "EWR":
            summary1 = ERWf[nf].describe()
         elif group1 == "JFK":
            summary1 = JFKf[nf].describe()
         else:
            summary1 = LGAf[nf].describe()

         if group2 == "EWR":
            summary2 = ERWf[nf].describe()
         elif group2 == "JFK":
            summary2 = JFKf[nf].describe()
         else:
            summary2 = LGAf[nf].describe()
         summary = pd.concat([summary1, summary2])
        st.dataframe(summary)