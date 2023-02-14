import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap
#from matplotlib.colors import SymLogNorm

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

if 'old_num_pts' not in st.session_state:
    st.session_state['old_num_pts'] = -1

def my_kernel(x, y, pt, kernel='poly', degree = 3, gamma = 1):
    if kernel == 'poly':
        return np.power(np.dot(np.array([xx,yy]),pt)+1,degree)
    elif kernel == 'rbf':
        dist = np.array([xx,yy])-pt
        return np.exp(-gamma*np.dot(dist,dist))
    elif kernel == 'sigmoid':
        return np.tanh(gamma *np.dot(np.array([xx,yy]),pt)+1)

col1, col2 = st.columns([2,3])

with col1:
    kernel = st.selectbox('Kernel to use:', 
            ('Polynomial', 'Radial basis function', 'Sigmoid'))
    
    if kernel == 'Polynomial':
        kernel = 'poly'
    elif kernel == 'Radial basis function':
        kernel = 'rbf'
    elif kernel == 'Sigmoid':
        kernel = 'sigmoid'

    num_pts = st.slider('Number of instances:', min_value = 1, max_value = 7)
    degree = 1
    gamma = 1
    if kernel == 'poly':
        degree = st.slider('Degree:', min_value = 1, max_value = 5)
    else:
        gamma = st.slider('gamma:', min_value=0.1, max_value=2.0, step = 0.1)
    
    new_pts = st.button('New points')
    if (st.session_state['old_num_pts'] != num_pts or new_pts):
        st.session_state.pts = np.array(4*np.random.rand(num_pts,2)-2)
        st.session_state['old_num_pts'] = num_pts

    pts = st.session_state.pts

    tabularView = st.checkbox('Tabular view')
    if tabularView:
        numDivisions = st.slider('Number of values in each direction', min_value=7, max_value = 25, step = 6)
        




with col2:
    if not tabularView:
        XX = np.linspace(-3,3,50)
        YY = np.linspace(-3,3,50)
        ZZ = np.zeros([ len(YY), len(XX)])
        i=0
        for xx in XX:
            j=0
            for yy in YY:
                zz = 0
                for pt in pts:
                    zz = zz + my_kernel(xx, yy, pt, kernel = kernel, gamma = gamma, degree=degree)
                ZZ[j,i]=zz
                j = j+1
            i=i+1
        fig, ax = plt.subplots()
        spread = np.max(ZZ)-np.min(ZZ)
        if spread > 10**3:
            if np.min(ZZ) < 0:
                log_levels = np.append(np.sort(-(10**np.arange(1,np.log10(-np.min(ZZ)), step = 1))), 0 )
            else:
                log_levels = []
            log_levels = np.append(log_levels, 10**np.arange(1, np.log10(np.max(ZZ))))
            CS = ax.contour(XX, YY, ZZ, levels=log_levels, colors='gray')
        else:
            CS = ax.contour(XX, YY, ZZ, colors='gray')
        ax.clabel(CS, inline=True, fontsize=10)
        if kernel == 'poly':
            ax.set_title('Polynomial with degree = '+ str(degree))
        elif kernel == 'rbf':
            ax.set_title('RBF with gamma = '+ str(gamma))
        elif kernel == 'sigmoid':
            ax.set_title('Sigmoid with gamma = '+ str(gamma))
        ax.set_aspect('equal', 'box')
        sns.scatterplot(x= pts[:,0],y =pts[:,1])
        plt.scatter(x= [0],y =[0], c = 'black', marker='+')

        st.pyplot(fig)
    
    else:
        
        XX = np.linspace(-3,3,numDivisions)
        YY = np.linspace(-3,3,numDivisions)
        ZZ = np.zeros([ len(YY), len(XX)])
        i=0
        for xx in XX:
            j=0
            for yy in YY:
                zz = 0
                for pt in pts:
                    zz = zz + my_kernel(xx, yy, pt, kernel = kernel, gamma = gamma, degree=degree)
                ZZ[j,i]=zz
                j = j+1
            i=i+1
        ZZ = np.round(ZZ, 2)
        ZZ = pd.DataFrame(ZZ, index = np.round(XX,2))
        ZZ.columns = np.round(YY,2)
        pdpts = pd.DataFrame(pts.transpose(), index = ['x','y'])
        st.caption("Instances")
        st.write(pdpts)
        st.write('''<div style="text-align: center;">x</div>''', unsafe_allow_html=True)
        st.write(ZZ)
    #st.text(log_levels)