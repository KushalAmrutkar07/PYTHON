from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():

    wine = datasets.load_wine()

    print(wine.feature_names)

    print(wine.target_names)

    print(wine.data[0:5])

    print(wine.target)

    x_train,x_test,y_train,y_test = train_test_split(wine.data,wine.target,test_size = 0.3)

    knn = KNeighborsClassifier(n_neighbors = 3)

    knn.fit(x_train,y_train)

    y_pred = knn.predict(x_test)

    
    print("Accuracy:",metrics.accuracy_score(y_test,y_pred)*100)

def main():

    print("----Marvellous Infosystem by Piyush Khairnar----")

    print("Machine Learning Application")

    print("Wine predictor application using K Nearest Kneighbor algorithm")

    WinePredictor()

if __name__ =="__main__":
    main()
