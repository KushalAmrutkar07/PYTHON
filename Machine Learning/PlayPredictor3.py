# Csv file madhuun read keli aahe

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


def MarvellousPlayPredictor(data_path):

    # step 1 : Load Data
    data = pd.read_csv(data_path,index_col=0)

    print("Size of Actual dataset",len(data))

    # step 2 : Clean , prepare and manipulate data
    feature_names = ['Whether','Temperature']

    print("Names of Features",feature_names)

    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # Creating labelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers
    weather_encoded = le.fit_transform(whether)
    print(weather_encoded)

    # Converting string labels into numbers
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    #combining weather and temp into single list of tupels
    features = list(zip(weather_encoded,temp_encoded))
    
    # step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training sets
    model.fit(features,label)

    #Step 4 : Test Data
    predicted = model.predict([[0,2]]) # 0 : Overcast, 2 : Mild
    print(predicted)

    if predicted:
        print("You can play")
    else:
        print("No Play")    

def main():
    print("Machine Learning Application")

    print("Play Predictor application using K Nearest Kneighbors algorithm")


    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ =="__main__":
    main()