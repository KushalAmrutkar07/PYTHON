# ha Recurssion aahe pan ha thambat nahi aahe
# Recurssion
# display 4 times Hello in Screen

def Display(No):
    if(No > 0):
        print("Hello")
        No = No-1
        Display(No)   #Recursive function call

Display(4)    #Function call
        