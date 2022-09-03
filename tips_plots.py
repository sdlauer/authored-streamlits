import streamlit as st
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# tips = sns.load_dataset('tips')
#
# def plots(x, y, hue, plot):
#     if plot=='Strip plot': sns.stripplot(x=x, y=y, hue=hue, data=tips)
#     if plot=='Box plot': sns.boxplot(x=x, y=y, hue=hue, data=tips)
#     if plot=='Swarm plot': sns.swarmplot(x=x, y=y, hue=hue, data=tips)
#     if plot=='Violin plot': sns.violinplot(x=x, y=y, hue=hue, data=tips)


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

st.title('Tips dataset')
