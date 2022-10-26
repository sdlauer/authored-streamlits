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

penguins = sns.load_dataset('penguins')
penguins.columns = ["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]
col1, col2 = st.columns([1,3])


tab1, tab2 = st.tabs(["Plot", "Summary statistics"])

with tab1:
    col1, col2 = st.columns([1.5,3])

    with col1:
        numerical = st.selectbox(
            "Numerical feature",
            ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
        )

        categorical = st.selectbox(
            "Categorical feature",
            ["species", "island","sex"]
        )

    with col2:
        fig, ax = plt.subplots()
        sns.kdeplot(x=numerical, data=penguins, hue=categorical)
        ax.set_xlabel(numerical, fontsize=14)
        ax.set_ylabel("Density", fontsize=14)
        ax.ticklabel_format(style='plain', axis='y')
        st.pyplot(fig)

with tab2:
        st.subheader("Summary statistics")
        summary = penguins[numerical].groupby(penguins[categorical]).describe()
        st.dataframe(summary)
