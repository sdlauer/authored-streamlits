# -*- coding: utf-8 -*-
"""
Created on Fri Nov 4 09:50:17 2022

@author: mrissler
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

@st.cache
@st.cache
def loadData():
    df = px.data.gapminder().query("year == 2007")
    df['logPop'] = np.log2(df['pop'])
    df['rootPop'] = np.sqrt(df['pop'])
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

col1, col2 = st.columns([1,3])

baseTextDesc = '''The horizontal axis is labeled "GDP per capita (\$/person)" and ranges from 0 to 50k.
The vertical axis is labeled "Life expectancy (years)" and ranges from 39 to 83.
Most points are follow a curve where low income (GDP per capita) countries (below \$2000) have low life expectancy (below 60 years),
but life expectancy increases rapidly with income with countries with an average income above \$5000 have a life expectancy above 70 years. '''

continentDesc = ''' Most low income/low life expectancy countries are from Africa.
European countries dominate the countries with high life expectancy.
Countries in Asia and the Americas make up many of the countries with relatively low income and high life expectancy.'''

with col1:
    plotType = st.selectbox('Color palette',
                            ('Default',
                             'Rainbow',
                             'Yellow-Green-Blue',
                             'Okabe-Ito'
                             'Contrast based',
                             'Shape based'))

    textDesc = st.checkbox('Text description of plot')

with col2:

    if plotType == "Rainbow":
        if textDesc:
            st.markdown(baseTextDesc+'''The continents for this plot are colored red for Asia, blue for Europe,
            green for Africa, purple for the Americas, and orange for Oceania.'''+continentDesc)


        else:
            fig = px.scatter(gm2007, x = 'gdpPercap', y = 'lifeExp',
                        color = 'continent', size = 'rootPop',
                        labels = {'gdpPercap' : 'GDP per capita ($/person)',
                                  'lifeExp' : 'Life expectancy (years)',
                                  'continent' : 'Continent',
                                  'rootPop': 'sqrt(Population)',
                                  'pop':'Population'},
                        hover_data={'gdpPercap':':.2f',
                                    'lifeExp':':.1f',
                                    'rootPop':False,
                                    'pop':True},
                        color_discrete_sequence = px.colors.qualitative.Set1,
                )
            fig.update_layout(font_size = 12,
                              legend=dict(yanchor="top", y=0.7, x=.75)
                              )
            st.plotly_chart(fig, use_container_width=True)

    elif plotType == "Yellow-Green-Blue":
        if textDesc:
            st.markdown(baseTextDesc+'''The continents for this plot are colored light yellow for Asia, yellow for Europe,
            yellow-green for Africa, green for the Americas, and blue for Oceania.
            The yellow colors are hard to see against the grey background.'''+continentDesc)


        else:
            fig = px.scatter(gm2007, x = 'gdpPercap', y = 'lifeExp',
                        color = 'continent', size = 'rootPop',
                        labels = {'gdpPercap' : 'GDP per capita ($/person)',
                                  'lifeExp' : 'Life expectancy (years)',
                                  'continent' : 'Continent',
                                  'rootPop': 'sqrt(Population)',
                                  'pop':'Population'},
                        hover_data={'gdpPercap':':.2f',
                                    'lifeExp':':.1f',
                                    'rootPop':False,
                                    'pop':True},
                        color_discrete_sequence = px.colors.colorbrewer.YlGnBu,
                )
            fig.update_layout(font_size = 12,
                              legend=dict(yanchor="top", y=0.7, x=.75)
                              )
            st.plotly_chart(fig, use_container_width=True)

    elif plotType == "Default":
        if textDesc:
            st.markdown(baseTextDesc+'''FIXME: The continents for this plot are colored light yellow for Asia, yellow for Europe,
            yellow-green for Africa, green for the Americas, and blue for Oceania.
            The yellow colors are hard to see against the grey background.'''+continentDesc)


        else:
            fig = px.scatter(gm2007, x = 'gdpPercap', y = 'lifeExp',
                        color = 'continent', size = 'rootPop',
                        labels = {'gdpPercap' : 'GDP per capita ($/person)',
                                  'lifeExp' : 'Life expectancy (years)',
                                  'continent' : 'Continent',
                                  'rootPop': 'sqrt(Population)',
                                  'pop':'Population'},
                        hover_data={'gdpPercap':':.2f',
                                    'lifeExp':':.1f',
                                    'rootPop':False,
                                    'pop':True},
                        color_discrete_sequence = ["#1f77b4","#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                                                   "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"],
                )
            fig.update_layout(font_size = 12,
                              legend=dict(yanchor="top", y=0.7, x=.75)
                              )
            st.plotly_chart(fig, use_container_width=True)

    elif plotType == "Contrast based":
        if textDesc:
            st.markdown(baseTextDesc+'''The continents for this plot are
            colored almost white for Asia, light grey for Europe,
            grey for Africa, grey blue for the Americas, and blue for Oceania.
            The light colors are hard to see against the grey background.'''+continentDesc)


        else:
            fig = px.scatter(gm2007, x = 'gdpPercap', y = 'lifeExp',
                        color = 'continent', size = 'rootPop',
                        labels = {'gdpPercap' : 'GDP per capita ($/person)',
                                  'lifeExp' : 'Life expectancy (years)',
                                  'continent' : 'Continent',
                                  'rootPop': 'sqrt(Population)',
                                  'pop':'Population'},
                        hover_data={'gdpPercap':':.2f',
                                    'lifeExp':':.1f',
                                    'rootPop':False,
                                    'pop':True},
                        color_discrete_sequence = px.colors.colorbrewer.Blues,
                )
            fig.update_layout(font_size = 12,
                              legend=dict(yanchor="top", y=0.7, x=.75)
                              )
            st.plotly_chart(fig, use_container_width=True)

    elif plotType == "Shape based":
        if textDesc:
            st.markdown(baseTextDesc+'''The continents for this plot are
            shown with green circles for Asia, orange diamonds for Europe,
            purple squares for Africa, pink x for the Americas, and green +
            for Oceania.'''+continentDesc)


        else:
            fig = px.scatter(gm2007, x = 'gdpPercap', y = 'lifeExp',
                        color = 'continent', size = 'rootPop',
                        symbol = 'continent',
                        labels = {'gdpPercap' : 'GDP per capita ($/person)',
                                  'lifeExp' : 'Life expectancy (years)',
                                  'continent' : 'Continent',
                                  'rootPop': 'sqrt(Population)',
                                  'pop':'Population'},
                        hover_data={'gdpPercap':':.2f',
                                    'lifeExp':':.1f',
                                    'rootPop':False,
                                    'pop':True},
                        color_discrete_sequence = px.colors.colorbrewer.Dark2,
                )
            fig.update_layout(font_size = 12,
                              legend=dict(yanchor="top", y=0.7, x=.75)
                              )
            st.plotly_chart(fig, use_container_width=True)

    else:
            st.text("Not implemented yet.")

st.header("Recommendation")
if plotType == "Rainbow":
    st.markdown('''The contrast between colors in rainbow scales
               are not usually uniformly spaced making distinguishing colors difficult for people
               with CVD. More disinguishable rainbow scales have been designed for situations
               where rainbow scales are commonly used. Ex: Temperature maps, radar maps.''')

elif plotType == "Yellow-Green-Blue":
    st.markdown('''Use a yellow-blue or green-blue color scale.
    By avoiding red, people with CVD are better
    able to distinguish colors.''')

elif plotType == "Contrast based":

    st.markdown('''Use a scale that depends on changes in contrast.
    By only changing the contrast, people with CVD can distinguish the
    colors as well as other people. But, some shades lack contrast with
    the background, emphasizing those with high contrast compared to the
    background.''')

elif plotType == "Shape based":

    st.markdown('''Use changes in another feature (size or shape).
    Users can depend on this other feature if the color scale is
    difficult to perceive.''')

else:
    st.text("Recommendations for this color scale not yet implemented")
