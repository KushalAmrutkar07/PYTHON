from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def MarvellousDecisionTreeClassifier():
    Dataset = load_iris()   # 1 Load the Data

    Data = Dataset.data
    Target = Dataset.target

    # 2 : Manipulate the data
    Data_train,Data_test,Target_train,Target_test = train_test_split(Data, Target,test_size = 0.5)

    Classifier = DecisionTreeClassifier()

    # 3 : Build the model
    Classifier.fit(Data_train,Target_train)

    # 4 : test the model
    Predictions = Classifier.predict(Data_test)
    
    Accuracy = accuracy_score(Target_test,Predictions)

    # 5 : Improve ---- Missing

    return Accuracy


def main():
    Ret = MarvellousDecisionTreeClassifier()

    print("Accuracy of Iris dataset with DesicionTree is :",Ret * 100)

if __name__=="__main__":
    main()