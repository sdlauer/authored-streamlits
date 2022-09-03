# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
#
# tips = sns.load_dataset('tips')
#
# # def plots(x, y, hue, plot):
# #     fig = plt.figure(figsize=(12, 6))
# #     if plot=='Strip plot': sns.stripplot(x=x, y=y, data=tips)
# #     if plot=='Box plot': sns.boxplot(x=x, y=y, hue=hue, data=tips)
# #     if plot=='Swarm plot': sns.swarmplot(x=x, y=y, hue=hue, data=tips)
# #     if plot=='Violin plot': sns.violinplot(x=x, y=y, hue=hue, data=tips)
# #     st.pyplot(fig)
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
# if plots == 'Strip plot': sns.stripplot(x='day', y='tips', data=tips)

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

st.header("Visualizing the tips dataset")
plot = st.selectbox(
    "Plot",
    [
        "violin plot",
        "strip plot",
        "box plot",
        "swarm plot"
    ]
)

categorical = st.selectbox(
    "Categorical variable",
    [
        "day",
        "time",
        "sex",
        "smoker"
    ]
)

numeric = st.selectbox(
    "Numeric variable",
    [
        "tip",
        "total_bill"
    ]
)

# group = st.selectbox(
#     "Grouping",
#     [
#         None,
#         "day",
#         "time",
#         "sex",
#         "smoker"
#     ]
# )

fig = plt.figure()

if plot == "violin plot":
    sns.violinplot(x=categorical, y=numeric, data = tips)

elif plot == "strip plot":
    sns.stripplot(x=categorical, y=numeric, data = tips)

elif plot == "Box plot":
    sns.boxplot(x=categorical, y=numeric, data = tips)

else:
    sns.swarmplot(x=categorical, y=numeric, data = tips)

st.pyplot(fig)
