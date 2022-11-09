import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import t

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

col1, col2 = st.columns([2,3])

with col1:
    distribution  =st.selectbox(
        "Distribution",
        [
            "binomial",
            "normal",
            "t"
        ]
    )
    st.text("Enter value or use - and +")
    if distribution == "binomial":
        nobs = st.number_input(
            "n",
            min_value=1,
            step=1,
            value=10,
            key=11
        )
        prob = st.number_input(
            label="Probability",
            min_value=0.00,
            max_value=1.00,
            value=0.50,
            step=0.01,
            key=12
        )
    elif distribution == "normal":
        meanmu = st.number_input(
            "Mean",
            value=0.0,
            step=0.1,
            key=13
        )
        stsigma = st.number_input(
            "Standard deviation",
            min_value=0.00,
            value=1.00,
            step=0.01,
            key=14
        )
    else:
        df = st.number_input(
            "Degrees of freedom (df)",
            min_value=0,
            step=1,
            value=10,
            key=15
        )

    check = st.checkbox("Add second distribution")

    if check:
        distribution2 = st.selectbox(
            "Distribution #2",
            [
                "binomial",
                "normal",
                "t"
            ]
        )
        if distribution2 == "binomial":
            nobs2 = st.number_input(
                "n",
                min_value=1,
                step=1,
                value=10,
                key=21
            )
            prob2 = st.number_input(
                label="Probability",
                min_value=0.00,
                max_value=1.00,
                value=0.50,
                step=0.01,
                key=22
            )
        elif distribution2 == "normal":
            meanmu2 = st.number_input(
                "Mean",
                value=0.0,
                step=0.1,
                key=23
            )
            stsigma2 = st.number_input(
                "Standard deviation",
                min_value=0.00,
                value=1.00,
                step=0.01,
                key=24
            )
        else:
            df2 = st.number_input(
                "Degrees of freedom (df)",
                min_value=0,
                step=1,
                value=10,
                key=25
            )

with col2:
    if check:
        fig, ax = plt.subplots()
        if distribution == "binomial":
            x = range(0, int(nobs)+1)
            ax.bar(x, height=binom.pmf(k=x, n=nobs, p=prob), width=0.75, alpha=0.5)
            ax.set(xlabel='X', ylabel="Probability")
            title1=("binomial( %02d, %0.2f)" %(nobs, prob))
        elif distribution == "normal":
            x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
            ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title1=('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
        else:
            x = np.linspace(t.ppf(0.0001, df=df), t.ppf(0.9999, df), 100)
            ax.plot(x, t.pdf(x=x, df=df), alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title1=('t(%02d)' %df)

        if distribution2 == "binomial":
            x2 = range(0, int(nobs2)+1)
            ax.bar(x2, height=binom.pmf(k=x2, n=nobs2, p=prob2), width=0.75, color='darkorange', alpha=0.5)
            ax.set(xlabel='X', ylabel="Probability")
            title2 = "binomial( %02d, %0.2f)" %(nobs2, prob2)
            ax.title.set_text("%s and %s" %(title1, title2))
            ax.legend([title1, title2])  
        elif distribution2 == "normal":
            x2 = np.linspace(norm.ppf(0.0001, meanmu2, stsigma2), norm.ppf(0.9999, meanmu2, stsigma2), 100)
            ax.plot(x2, norm.pdf(x=x2, loc=meanmu2, scale=stsigma2), color='darkorange', alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title2 = 'normal(%0.2f, %0.2f)' %(meanmu2, stsigma2)
            ax.title.set_text('%s and %s' %(title1, title2))
            ax.legend([title1, title2])
        else:
            x2 = np.linspace(t.ppf(0.0001, df=df2), t.ppf(0.9999, df2), 100)
            ax.plot(x2, t.pdf(x=x2, df=df2), color='darkorange', alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title2 = 't(%02d)' %(df2)
            ax.title.set_text('%s and %s' %(title1, title2))
            ax.legend([title1, title2])              
    else:
        fig, ax = plt.subplots()
        if distribution == "binomial":
            x = range(0, int(nobs)+1)
            ax.bar(x, height=binom.pmf(k=x, n=nobs, p=prob), width=0.75)
            ax.set(xlabel='X', ylabel="Probability")
            title1 = "binomial( %02d, %0.2f)" %(nobs, prob)
            ax.title.set_text(title1)
        elif distribution == "normal":
            x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
            ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma))
            ax.set(xlabel='X', ylabel='Density')
            title1 = ('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
            ax.title.set_text(title1)
        else:
            x = np.linspace(t.ppf(0.0001, df=df), t.ppf(0.9999, df), 100)
            ax.plot(x, t.pdf(x=x, df=df))
            ax.set(xlabel='X', ylabel='Density')
            title1 = 't(%02d)' %df
            ax.title.set_text(title1)

    st.pyplot(fig)
    check2 = st.checkbox("Description")
    if check2:
        if check:
            if distribution == "binomial":
                mean1=nobs*prob
                stdev1=(nobs*(prob)*(1-prob))**0.5
                lower1=int(binom.ppf(0.001, nobs, prob))
                upper1=int(binom.ppf(0.999, nobs, prob))
                alttext1= "Probability distribution graph of a %s distribution. The distribution \
                has a mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %02d \
                and the 0.999 quantile is %02d." %(title1, mean1, stdev1, lower1, upper1)
            elif distribution == "t":
                mean1=0
                stdev1=(df/(df-2))**0.5
                lower1=t.ppf(0.001, df)
                upper1=t.ppf(0.999, df)
                alttext1= "Probability distribution curve of a %s distribution. The distribution \
                is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
                of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
                %(title1, mean1, stdev1, lower1, upper1)
            else:
                mean1=meanmu
                stdev1=stsigma
                lower1=norm.ppf(0.001, meanmu, stsigma)
                upper1=norm.ppf(0.999, meanmu, stsigma)
                alttext1= "Probability distribution curve of a %s distribution. The distribution \
                is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
                of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
                %(title1, mean1, stdev1, lower1, upper1)

            if distribution2 == "binomial":
                mean2=nobs2*prob2
                stdev2=(nobs2*(prob2)*(1-prob2))**0.5
                lower2=int(binom.ppf(0.001, nobs2, prob2))
                upper2=int(binom.ppf(0.999, nobs2, prob2))
                alttext2= "A second distribution is also shown of the probability distribution graph \
                of a %s distribution. The distribution has a mean of %0.2f and a standard deviation \
                of %0.2f. The 0.001 quantile is %02d and the 0.999 quantile is %02d." \
                %(title2, mean2, stdev2, lower2, upper2)
            elif distribution2== "t":
                mean2=0
                stdev2=(df2/(df2-2))**0.5
                lower2=t.ppf(0.001, df2)
                upper2=t.ppf(0.999, df2)
                alttext2= "A second distribution is also shown of the probability distribution curve \
                of a %s distribution. The distribution is unomodal, symmetric, and bell-shaped with a \
                mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %0.2f and the \
                0.999 quantile is %0.2f." %(title2, mean2, stdev2, lower2, upper2)
            else:
                mean2=meanmu2
                stdev2=stsigma2
                lower2=norm.ppf(0.001, meanmu2, stsigma2)
                upper2=norm.ppf(0.999, meanmu2, stsigma2)
                alttext2= "A second distribution is also shown of the probability distribution curve \
                of a %s distribution. The distribution is unomodal, symmetric, and bell-shaped with a \
                mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %0.2f and the \
                0.999 quantile is %0.2f." %(title2, mean2, stdev2, lower2, upper2)  
            st.write(alttext1 + alttext2)          
        else:
            if distribution == "binomial":
                mean1=nobs*prob
                stdev1=(nobs*(prob)*(1-prob))**0.5
                lower1=int(binom.ppf(0.001, nobs, prob))
                upper1=int(binom.ppf(0.999, nobs, prob))
                alttext1= "Probability distribution graph of a %s distribution. The distribution \
                has a mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %02d \
                and the 0.999 quantile is %02d." %(title1, mean1, stdev1, lower1, upper1)
            elif distribution == "t":
                mean1=0
                stdev1=(df/(df-2))**0.5
                lower1=t.ppf(0.001, df)
                upper1=t.ppf(0.999, df)
                alttext1= "Probability distribution curve of a %s distribution. The distribution \
                is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
                of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
                %(title1, mean1, stdev1, lower1, upper1)
            else:
                mean1=meanmu
                stdev1=stsigma
                lower1=norm.ppf(0.001, meanmu, stsigma)
                upper1=norm.ppf(0.999, meanmu, stsigma)
                alttext1= "Probability distribution curve of a %s distribution. The distribution \
                is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
                of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
                %(title1, mean1, stdev1, lower1, upper1)
            st.write(alttext1)
