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

	if group1 == "EWR":
		data1 = EWRf
	elif group1 == "JFK":
		data1 = JFKf
	elif group1 == "LGA":
		data1 = LGAf
	else:
		data1=flights

	group2 = st.selectbox(
		"Group 2",
		[
			"none",
			"EWR",
			"JFK",
			"LGA"
		]
	)

	if group2 == "EWR":
		data2 = EWRf
	elif group2 == "JFK":
		data2 = JFKf
	elif group2 == "LGA":
		data2 = LGAf
	else:
		data2=flights

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
			summary = flights[nf].describe().apply("{0:.2f}".format)
			summary=summary.rename("All" + ' ' + numerical)
		elif group1 != "none" and group2 == "none":
			if group1 == "EWR":
				summary = EWRf[nf].describe().apply("{0:.2f}".format)
				summary=summary.rename(group1 + ' ' + numerical)
			elif group1 == "JFK":
				summary = JFKf[nf].describe().apply("{0:.2f}".format)
				summary=summary.rename(group1 + ' ' + numerical)
			else:
				summary = LGAf[nf].describe().apply("{0:.2f}".format)
				summary=summary.rename(group1 + ' ' + numerical)
		elif group1 == "none" and group2 != "none":
			if group2 == "EWR":
				summary = EWRf[nf].describe().apply("{0:.2f}".format)
				summary=summary.rename(group2 + ' ' + numerical)
			elif group2 == "JFK":
				summary = JFKf[nf].describe().apply("{0:.2f}".format)
				summary=summary.rename(group2 + ' ' + numerical)
			else:
				summary = LGAf[nf].describe().apply("{0:.2f}".format)
				summary=summary.rename(group2 + ' ' + numerical)
		else:
			if group1 == "EWR":
				summary1 = EWRf[nf].describe().apply("{0:.2f}".format)
				summary1=summary1.rename('G1: '+ group1)
			elif group1 == "JFK":
				summary1 = JFKf[nf].describe().apply("{0:.2f}".format)
				summary1=summary1.rename('G1: '+ group1)
			else:
				summary1 = LGAf[nf].describe().apply("{0:.2f}".format)
				summary1=summary1.rename('G1: '+ group1)
			if group2 == "EWR":
				summary2 = EWRf[nf].describe().apply("{0:.2f}".format)
				summary2=summary2.rename('G2: '+ group2)
			elif group2 == "JFK":
				summary2 = JFKf[nf].describe().apply("{0:.2f}".format)
				summary2=summary2.rename('G2: '+ group2)
			else:
				summary2 = LGAf[nf].describe().apply("{0:.2f}".format)
				summary2=summary2.rename('G2: '+ group2)
			summary = pd.concat([summary1, summary2], axis=1)
		#summary.columns = ["Count","Mean","Std", "Min", "Q1", "Median", "Q3", "Max"]
		st.dataframe(summary)

with col2:
	fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
	if group1 == "none" and group2 == "none":
		ax1.hist(x=flights[nf])
		ax1.title.set_text('All flights')
		ax1.set(xlabel='%s (minutes)' %numerical, ylabel="Counts")
		ax2.axis('off')
	elif group1 != "none" and group2 == "none":
		ax1.hist(x=data1[nf])
		ax1.title.set_text('Flights from %s' %group1)
		ax1.set(xlabel='%s (minutes)' %numerical, ylabel="Counts")
		ax2.axis('off')
	elif group1 == "none" and group2 != "none":
		ax2.hist(x=data2[nf])
		ax2.title.set_text('Flights from %s' %group2)
		ax2.set(xlabel='%s (minutes)' %numerical, ylabel="Counts")
		ax1.axis('off')
	else:
		ax1.hist(x=data1[nf])
		ax1.title.set_text('Flights from %s' %group1)
		ax1.set(xlabel='%s (minutes)' %numerical, ylabel="Counts")
		ax2.hist(x=data2[nf])
		ax2.title.set_text('Flights from %s' %group2)
		ax2.set(xlabel='%s (minutes)' %numerical, ylabel="Counts")
	fig.tight_layout(pad=1.0)
	st.pyplot(fig)

	if group1 != "none" and group2 != "none":
		if alternative == "not equal":
			hyptest = ttest_ind(a=data1[nf], b=data2[nf], equal_var=True, alternative='two-sided')
		elif alternative == "less than":
			hyptest = ttest_ind(a=data1[nf], b=data2[nf], equal_var=True, alternative='less')
		else:
			hyptest = ttest_ind(a=data1[nf], b=data2[nf], equal_var=True, alternative='greater')
		st.write('Test statistic:', hyptest[0])
		st.write('p-value: ', hyptest[1])
	else:
		st.write('Select Group 1 and Group 2 for hypothesis test')