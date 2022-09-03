import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# tips = px.data.tips()
#
# def plots(x, y, hue, plot):
#     if plot=='Strip plot': px.strip(tips, x=x, y=y)
#     # if plot=='Box plot': sns.boxplot(x=x, y=y, hue=hue, data=tips)
#     # if plot=='Swarm plot': sns.swarmplot(x=x, y=y, hue=hue, data=tips)
#     # if plot=='Violin plot': sns.violinplot(x=x, y=y, hue=hue, data=tips)
#
# st.title('Visualizing the tips dataset')
#
# plots = st.selectbox(
#      'Select plot',
#      ('Strip plot', 'Box plot', 'Swarm plot','Violin plot'))
#
# hue = st.selectbox(
#      'Select hue',
#      (None,'sex', 'smoker', 'day','time'))
#
# x = st.selectbox(
#      'Select categorical variable',
#      ('sex', 'smoker', 'day','time'))
#
# y = st.selectbox(
#      'Select numerical variable',
#      ('tip','total_bill'))
#
# if plots == 'Strip plot': plots(x,y,hue,'Strip plot')
# # elif plots == 'Box plot': plots(x,y,hue,'Box plot')
# # elif plots == 'Swarm plot': plots(x,y,hue,'Swarm plot')
# # else: plots(x,y,hue,'Violin plot')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
