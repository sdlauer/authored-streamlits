import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


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

#st.header("Finding the maximal margin hyperplane")

url = "https://raw.githubusercontent.com/aimeeschwab-mccoy/streamlit_asm/main/forest_fires.csv"

fires = pd.read_csv(url).sample(20, random_state=1)
fires.columns = list(fires.columns)

# Define input and output features
X = fires[['Temp', 'Humidity']]
y = fires[['Fire']]

# Relabel some instances for full separation
y.at[113,'Fire']=1
y.at[119,'Fire']=1
y.at[46,'Fire']=0
y.at[67,'Fire']=0

y2 = np.ravel(y)
y2[y2==0] = -1

# Scale the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert scaled inputs back to a dataframe
X = pd.DataFrame(X_scaled, index=X.index, columns=X.columns)
X = X.reset_index(drop=True)

col1, col2 = st.columns([2,3])

with col1:

    alphas = np.zeros(20)
    #st.write("$\\alpha_1$")

    alphas[1] = st.slider(label="\$ \\alpha \$ &alpha;1: Choose a value between 0 and 3.0.", min_value=0.0, max_value=3.0, value=0.0, step=0.01)

    #st.write("$\\alpha_2$")

    alphas[2] = st.slider(label="a2: Choose a value between 0 and 3.0.", min_value=0.0, max_value=3.0, value=0.0, step=0.01)

    #st.write("$\\alpha_6$")

    alphas[6] = st.slider(label="a6: Choose a value between 0 and 3.0.", min_value=0.0, max_value=3.0, value=0.0, step=0.01)

    #st.write("$\\alpha_{11}$")

    alphas[11] = st.slider(label="a11: Choose a value between 0 and 3.0.", min_value=0.0, max_value=3.0, value=0.0, step=0.01)
    
    #st.write("$\\alpha_{13}$")

    alphas[13] = st.slider(label="a13: Choose a value between 0 and 3.0.", min_value=0.0, max_value=3.0, value=0.0, step=0.01)

    weights = np.multiply(np.array(alphas),np.array(y2))*np.matrix(X)

    a = - weights[0,0]/weights[0,1]
    b = -np.sum(np.multiply(np.ravel(np.matrix(X[np.abs(alphas)>0.01])*weights.T), alphas[alphas>0]))/np.sum(alphas) / weights[0,1]
    xx = np.linspace(-3, 3)
    yy = a * xx - b
    
    showmargin = st.checkbox(label="Show minimal target hyperplane?", value=False)

   

with col2:

    fig, ax = plt.subplots()

    p = sns.scatterplot(data=X, x='Temp', y='Humidity', hue=np.ravel(y), 
        style=np.ravel(y), palette='deep')
    p.set_ylabel("Humidity", fontsize=14)
    p.set_xlabel("Temperature", fontsize=14)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    plt.legend(labels=['Fire', 'No fire'])
    for i, point in X.iterrows():
        ax.text(point['Temp'], point['Humidity'], str(i))
    plt.plot(xx, yy, 'red')

    if showmargin:
        a2 = 0.596492574115393 
        xx2 = np.linspace(-3, 3)
        yy2 = a2 * xx2 - 0.59274499
        plt.plot(xx2, yy2, 'black')

    st.pyplot(fig)

    showtext = st.checkbox(label="Show description?", value=False)

    if showtext:

        st.write('''The scatterplot shows standardized temperature on the horizontal axis and standardized humidity on the vertical axis. Both features range from -3 to +3. A hyperplane separates two classes. Instances below the hyperplane have high temperatures, low humidity, 
        and are classified as Fire. Instances above the hyperplane have low temperatures, high humidity, and are classified as No fire.''')

    if showmargin:
        st.write("The minimal target hyperplane has $\\alpha_1$ = 0.96, $\\alpha_2$ = 1.73,  $\\alpha_6$ = 2.70, $\\alpha_{11}$ = 0 and $\\alpha_{13}$ = 0.")

    constraint = (np.matrix(alphas)*np.matrix(y2).T)[0,0]

    st.write("$\\sum_{j=1}^p y_j \\alpha_j $=", round(constraint, 3), "=0?")

    total = (np.matrix(alphas)*(np.matrix(y2).T*np.matrix(y2)*(np.matrix( X)*np.matrix(X).T))*np.matrix(alphas).T/2.0 - np.sum(alphas))[0,0]

    st.write("Target = ", round(total,2))


