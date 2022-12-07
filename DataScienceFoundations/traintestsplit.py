# Import packages
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import r_regression

#Apologies in advance for messy formatting

#set the seed
np.random.seed(12345)


# Load bad drivers data
badDrivers = pd.read_csv('bad-drivers.csv')



hide = """
        <style>
        max-width: {max_width:400}px;
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {overflow: hidden;}
        div.block-container {padding-top:1rem;}
        div.block-container {padding-bottom:1rem;}
        </style>
        """


# Select the proportions of the training-validation-test split using a slider
a,b = st.slider("Select cutoffs for the training-validation-test split percentages",
    min_value=0, max_value=100, value=(70,80), step=1)

trainingProportion = a / 100
validationProportion = (b-a)/100
testProportion = 1 - trainingProportion - validationProportion



if a < 3 or a == b or b == 100:
    st.write("The data will be split into training, validation, and test data. All three sets should be nonempty, so the cutoffs should be distinct, not 0, and not 100.")
else:
    # Split off the test data
    trainingAndValidationData, testData = train_test_split(
        badDrivers,
        test_size=testProportion
        )
        # Split the remaining into training and validation data
    trainingData, validationData = train_test_split(
        trainingAndValidationData,
        train_size=trainingProportion/(trainingProportion+validationProportion)
        )

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write("Training data: ",a, "%  \n  ",
        "n: ",len(trainingData), "  \n  ",
        "x mean: ", (trainingData[['Losses incurred by insurance companies for collisions per insured driver ($)']].apply(np.mean))[0].astype(int), "  \n  ",
        "x sd: ", (trainingData[['Losses incurred by insurance companies for collisions per insured driver ($)']].apply(np.std))[0].astype(int), "  \n  ",
        "y mean: ", (trainingData[['Car Insurance Premiums ($)']].apply(np.mean))[0].astype(int), "  \n  ",
        "y sd: ", (trainingData[['Car Insurance Premiums ($)']].apply(np.std))[0].astype(int), "  \n  ",
        "r: ", np.round(r_regression(trainingData[['Losses incurred by insurance companies for collisions per insured driver ($)']].values,np.ravel(trainingData[['Car Insurance Premiums ($)']].values))[0],3) )

        includeTraining = st.checkbox('Graph training data', key="check1", value=True)

    with col2:
        st.write("Validation data: ",(b-a), "%  \n  ",
        "n: ",len(validationData), "  \n  ",
        "x mean: ", (validationData[['Losses incurred by insurance companies for collisions per insured driver ($)']].apply(np.mean))[0].astype(int), "  \n  ",
        "x sd: ", (validationData[['Losses incurred by insurance companies for collisions per insured driver ($)']].apply(np.std))[0].astype(int), "  \n  ",
        "y mean: ", (validationData[['Car Insurance Premiums ($)']].apply(np.mean))[0].astype(int), "  \n  ",
        "y sd: ", (validationData[['Car Insurance Premiums ($)']].apply(np.std))[0].astype(int), "  \n  ",
        "r: ", np.round(r_regression(validationData[['Losses incurred by insurance companies for collisions per insured driver ($)']].values,np.ravel(validationData[['Car Insurance Premiums ($)']].values))[0],3) )

        includeValidation = st.checkbox('Graph validation data', key="check2", value=True)

    with col3:
        st.write("Test data: ",(100-b), "%  \n  ",
        "n: ",len(testData), "  \n  ",
        "x mean: ", (testData[['Losses incurred by insurance companies for collisions per insured driver ($)']].apply(np.mean))[0].astype(int), "  \n  ",
        "x sd: ", (testData[['Losses incurred by insurance companies for collisions per insured driver ($)']].apply(np.std))[0].astype(int), "  \n  ",
        "y mean: ", (testData[['Car Insurance Premiums ($)']].apply(np.mean))[0].astype(int), "  \n  ",
        "y sd: ", (testData[['Car Insurance Premiums ($)']].apply(np.std))[0].astype(int), "  \n  ",
        "r: ", np.round(r_regression(testData[['Losses incurred by insurance companies for collisions per insured driver ($)']].values,np.ravel(testData[['Car Insurance Premiums ($)']].values))[0],3) )

        includeTest = st.checkbox('Graph test data', key="check3", value=True)


#Create the scatterplot.
    plt.scatter(
        badDrivers[['Losses incurred by insurance companies for collisions per insured driver ($)']],
        badDrivers[['Car Insurance Premiums ($)']],c="#FFFFFF")

    if includeTraining:
        plt.scatter(
            trainingData[['Losses incurred by insurance companies for collisions per insured driver ($)']],
            trainingData[['Car Insurance Premiums ($)']], c="#fde725")

    if includeValidation:
        plt.scatter(
            validationData[['Losses incurred by insurance companies for collisions per insured driver ($)']],
            validationData[['Car Insurance Premiums ($)']], c="#21918c")

    if includeTest:
        plt.scatter(
            testData[['Losses incurred by insurance companies for collisions per insured driver ($)']],
            testData[['Car Insurance Premiums ($)']], c="#440154")

#Create the legend
    patch1 = mpatches.Patch(color='#fde725', label='Training data')
    patch2 = mpatches.Patch(color='#21918c', label='Validation data')
    patch3 = mpatches.Patch(color='#440154', label='Test data')
    plt.legend(handles=[patch1, patch2, patch3])

#Format the plot area
    plt.xlabel('Losses incurred by insurance companies', fontsize=14)
    plt.ylabel('Car insurance premiums',fontsize=14)
    plt.xlim(80,200)
    plt.ylim(600,1400)
    plt.title('Traning-validation-test split')

#I couldn't get the resizing to work to my satisfaction, so I used columns as a hackey way to keep the graph small and centered.
    cola, colb, colc = st.columns([1,3,1])
    with colb:
        st.pyplot(plt)
    st.write("Description: The training data, validation data, and testing data have similar but not identical distributions. The more evenly split the data is, the more similar the distributions are.")
