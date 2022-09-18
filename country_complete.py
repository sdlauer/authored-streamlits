import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

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

country = pd.read_csv("country_complete.csv")


tab1, tab2 = st.tabs(["Plot", "Summary statistics"])

with tab1:
    col1, col2 = st.columns([2,3])

    with col1:
        plot = st.selectbox(
            "Plot",
            [
                "Box plot",
                "Density plot",
                "Histogram"
            ]
        )

        numerical = st.selectbox(
            "Numerical feature",
            [
                "Years",
                "Fertility",
                "Emissions",
                "Internet"
            ]
        )

        continent = st.selectbox(
            "Continent",
            [
                "Africa",
                "Americas",
                "Asia",
                "Europe",
                "Oceania"
            ]
        )

    with col2:
        df = country[country["Continent"]==continent][numerical]
        fig, ax = plt.subplots()

        if plot == "Box plot":
            sns.boxplot(x=df, width=0.5)

        elif plot == "Histogram":
            sns.histplot(x=df)

        elif plot == "Density plot":
            sns.histplot(x=df, kde=True)

        ax.set_xlabel(numerical, fontsize=14)
        ax.ticklabel_format(style='plain', axis='x')

        if plot=="Histogram": ax.set_ylabel("Count", fontsize=14)
        if plot=="Density plot":
            ax.set_ylabel("Count", fontsize=14)
            ax.ticklabel_format(style='plain', axis='y')

        st.pyplot(fig)

with tab2:
        for i in ["Africa","Americas","Asia","Europe","Oceania"]:
            if i!="Americas":
                st.subheader("Five number summary for " + i)
            else: st.subheader("Five number summary for the Americas")
            five_num = country[country["Continent"]==i].describe()
            st.dataframe(five_num)

        # st.subheader("Five number summary for Africa")
        # five_num_africa = country[country["Continent"]=="Africa"].describe()
        # st.dataframe(five_num_africa)
        #
        # st.subheader("Five number summary for Americas")
        # five_num_africa = country[country["Continent"]=="Americas"].describe()
        # st.dataframe(five_num_americas)
        #
        # st.subheader("Five number summary for Asia")
        # five_num_africa = country[country["Continent"]=="Asia""].describe()
        # st.dataframe(five_num_asia)
        #
        # st.subheader("Five number summary for Europe")
        # five_num_africa = country[country["Continent"]=="Europe"].describe()
        # st.dataframe(five_num_europe)
        #
        # st.subheader("Five number summary for Oceania")
        # five_num_africa = country[country["Continent"]=="Oceania"].describe()
        # st.dataframe(five_num_africa)
