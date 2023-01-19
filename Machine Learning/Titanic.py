# Logistic madhli case aahe hi

import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def MarvellousTitanicLogistic():
    #step 1: Load data
    titanic_data = pd.read_csv('MarvellousTitanicDataset.csv')

    print("First 5 entries from loaded dataset")

    print()

    print(titanic_data.head())
    
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Number of passangers are "+str(len(titanic_data)))

    #Step 2: Analyze data

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Visualisation : Survived and non Survived passengers")
    figure()
    target = "Survived"

    countplot(data = titanic_data,x = target).set_title("Marvellous Infosystem: Survived and non survived passengers")
    show()

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Visualisation : Survived and non Survived passengers based on Gender")
    figure()
    target = "Survived"

    countplot(data = titanic_data,x = target,hue ="Sex").set_title("Marvellous Infosystem: Survived and non survived passengers based on Gender")
    show()
    
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Visualisation : Survived and non Survived passengers based on Passenger class")
    figure()
    target = "Survived"

    countplot(data = titanic_data,x = target,hue ="Pclass").set_title("Marvellous Infosystem: Survived and non survived passengers based on the Passenger class")
    show()

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Visualisation : Survived and non Survived passengers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Marvellous Infosystem: Survived and non survived passengers based on the Age")
    show()
    
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Visualisation : Survived and non Survived passengers based on the Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Marvellous Infosystem: Survived and non survived passengers based on the Fare")
    show()
    
   # Step 3 : Data Cleaning

    titanic_data.drop("zero",axis = 1 , inplace = True)
    
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("First 5 entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))
    
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Values of Sex coloumn after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"],drop_first = True)
    print(Sex.head(5))

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Values of PClass coloumn after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"],drop_first = True)
    print(Pclass.head(5))

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Values of data set after concatenating new coloumns")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis = 1)
    print(titanic_data.head(5))
    
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Values of data set after removing irrelevent coloumns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis = 1, inplace= True)
    print(titanic_data.head(5))

    print()
    print("----------------------------------------------------------------------------------------------")
    
    x = titanic_data.drop("Survived",axis=1)
    y = titanic_data["Survived"]

    # Step 4  : Data Training

    xtrain , xtest, ytrain,ytest = train_test_split(x,y,test_size = 0.5)
    
    logmodel = LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    # step 5 : Data Testing 
    prediction = logmodel.predict(xtest)

    # step 6 : Calualte Accuracy 
    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Classification report of Logistic Regression is :")
    print(classification_report(ytest,prediction))

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Confusion Matrix of Logistic Regression is :")
    print(confusion_matrix(ytest,prediction))

    print()
    print("----------------------------------------------------------------------------------------------")
    
    print("Accuracy of Logistic Regression is :")
    print(accuracy_score(ytest,prediction))

    print()
    print("----------------------------------------------------------------------------------------------")
    
def main():

    
    MarvellousTitanicLogistic()

if __name__ =="__main__":
    main()
    


