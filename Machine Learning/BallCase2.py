# case study in Ml pip install scikit-learn 
# encoding karaychi aahe

# load the dataset
# Rough 1
# Smooth 0

# Tennis 1
# cricket 2

from sklearn import tree

Features =[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

obj = tree.DecisionTreeClassifier()

obj = obj.fit(Features,Labels) # Training

print(obj.predict([[97,0],[35,1]]))

         