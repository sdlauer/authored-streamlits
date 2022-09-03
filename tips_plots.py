import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

def plots(x, y, hue, plot):
    if plot=='Strip plot': sns.stripplot(x=x, y=y, hue=hue, data=tips)
    if plot=='Box plot': sns.boxplot(x=x, y=y, hue=hue, data=tips)
    if plot=='Swarm plot': sns.swarmplot(x=x, y=y, hue=hue, data=tips)
    if plot=='Violin plot': sns.violinplot(x=x, y=y, hue=hue, data=tips)

st.title('Visualizing the tips dataset')

plots = st.selectbox(
     'Select plot',
     ('Strip plot', 'Box plot', 'Swarm plot','Violin plot'))

hue = st.selectbox(
     'Select hue',
     (None,'sex', 'smoker', 'day','time'))

x = st.selectbox(
     'Select categorical variable',
     ('sex', 'smoker', 'day','time'))

y = st.selectbox(
     'Select numerical variable',
     ('tip','total_bill'))

if plots == 'Violin plot': plots(x,y,hue,'Strip plot')
elif plots == 'Box plot': plots(x,y,hue,'Box plot')
elif plots == 'Swarm plot': plots(x,y,hue,'Swarm plot')
else: plots(x,y,hue,'Violin plot')
