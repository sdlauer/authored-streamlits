# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import streamlit as st
#
# st.title("Regression using the mpg dataset")
#
# tips = sns.load_dataset("tips")
#
# reg_line = st.checkbox("Regression line")
# reg_eq = st.checkbox("Regression equation")
# corr_coef = st.checkbox("Correlation coefficient")
#
# input = st.selectbox(
#     "Input feature",
#     [
#         "tip",
#         "total_bill"
#         # "mpg",
#         # "cylinders",
#         # "displacement",
#         # "horsepower",
#         # "weight",
#         # "acceleration",
#         # "model_year",
#         # "origin",
#         # "name"
#     ]
# )
#
# output = st.selectbox(
#     "Output feature",
#     [
#         "tip",
#         "total_bill"
#         # "mpg",
#         # "cylinders",
#         # "displacement",
#         # "horsepower",
#         # "weight",
#         # "acceleration",
#         # "model_year",
#         # "origin",
#         # "name"
#     ]
# )
#
# fig = plt.figure()
# sns.scatterplot(x=input, y=output, data=tips)
# st.pyplot(fig)

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

mpg=pd.read_csv("mpg.csv")

st.header("Visualizing the tips dataset")

input_feat = st.selectbox(
    "Input feature",
    [
        "mpg",
        "cylinders",
        "displacement",
        "horsepower",
        "weight",
        "acceleration",
        "model_year",
        "origin",
        "name"
    ]
)

output_feat = st.selectbox(
    "Output feature",
    [
        "mpg",
        "cylinders",
        "displacement",
        "horsepower",
        "weight",
        "acceleration",
        "model_year",
        "origin",
        "name"
    ]
)
fig = plt.figure()
sns.scatterplot(x=input_feat, y=output_feat, data=mpg)
st.pyplot(fig)
