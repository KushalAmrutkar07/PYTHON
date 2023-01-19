import pandas as pd
import seaborn as sns
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

def MarvellousSVMIris(URL):
    colnames = ["sepal_length_in_cm","sepal_width_in_cm","petal_length_in_cm","petal_width_in_cm","class"]

    dataset = pd.read_csv(URL,header = None,names=colnames)
    print("Dataset loaded succesfully")

    print("Dataset is ")
    print(dataset.head())

    dataset = dataset.replace({"class":{"Iris-setosa":1,"Iris-versicolor":2,"Iris-virginica":3}})
    print("After encoding dataset is : ")
    print(dataset.head())

    X = dataset.iloc[:,:-1]
    y = dataset.iloc[:,-1].values

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25,random_state = 0)

    classifier = SVC(kernel = 'linear', random_state = 0)
    classifier.fit(X_train,y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test,y_pred)
    print(cm)

    accuracies = cross_val_score(estimator = classifier , X = X_train , y = y_train ,cv = 10)
    print("Accuracy : {:.2f} %".format(accuracies.mean()*100))
   
def main():
    print("_______Marvellous Support Vector Machine_______")

    MarvellousSVMIris("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

if __name__=="__main__":
    main()
