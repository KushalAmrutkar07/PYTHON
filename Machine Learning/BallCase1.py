# case study in Ml pip install scikit-learn

# Import required Library
from sklearn import tree

Features =[[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]] 
Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

# DECIDE THE MACHINE LEARNING ALGORITHM
obj = tree.DecisionTreeClassifier()

obj = obj.fit(Features,Labels) # Training

print(obj.predict([[97,"Smooth"]]))

         