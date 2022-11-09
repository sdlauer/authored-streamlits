# -*- coding: utf-8 -*-
"""
Created on Fri Nov 4 09:50:17 2022

@author: mrissler
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

@st.cache
@st.cache
def loadData():
    df = px.data.gapminder().query("year == 2007")
    return df


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

gm2007 = loadData()

tab1, tab2 = st.tabs(["Recommendations", "Playground"])

with tab1:
    col1, col2 = st.columns([1,4])

    with col1:
        plotType = st.selectbox('Type of color scale',
                                ('Rainbow',
                                 'Yellow-Blue',
                                 'Contrast based',
                                 'Shape based'))

        textDesc = st.checkbox('Text descriptions of plot')

    with col2:

        if plotType == "Rainbow":
                fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp',
                            color = 'continent', size = 'logPop',
                            labels = {'gdpPercap' : 'GDP per capita ($/person)',
                                      'lifeExp' : 'Life expectancy (years)',
                                      'continent' : 'Continent',
                                      'logPop': 'log(Population)'},
                            color_discrete_sequence = px.colors.qualitative.Set1,
                    )
                fig.update_layout(font_size = 12,
                                  legend=dict(yanchor="top", y=0.7, x=.75)
                                  )
                st.plotly_chart(fig, use_container_width=True)

        else:
                st.text("Not implemented yet.")
    st.text("Recommendations for this color scale")
