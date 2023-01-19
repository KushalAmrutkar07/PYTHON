# Diabetes Predictor using Logistic Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter

print("-----Diabetes predictor using Logistic Regression ----")

simplefilter(action ='ignore',category=FutureWarning)

diabetes = pd.read_csv('diabetes.csv')

print("Coloumns of Dataset")
print(diabetes.columns)

print("First 5 records of datasets")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

X_train,X_test,y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify = diabetes['Outcome'], random_state = 66)

logreg = LogisticRegression().fit(X_train,y_train)

print("Training set Accuracy: {:.3f}".format(logreg.score(X_train,y_train)))

print("Test set Accuracy: {:.3f}".format(logreg.score(X_test,y_test)))

logreg001 = LogisticRegression(C = 0.01).fit(X_train,y_train)

print("Training set Accuracy: {:.3f}".format(logreg001.score(X_train,y_train)*100))

print("Test set Accuracy: {:.3f}".format(logreg001.score(X_test,y_test)*100))

