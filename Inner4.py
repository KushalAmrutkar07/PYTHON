# User defined Decoration

def Outer():
    print("Inside outer")   #2

    def Inner():
        print("Inside Inner")  #4
    
    print(id(Inner))
    return Inner #3

ret = Outer()   #1

print(type(ret))

print(id(ret))

ret()   #4()    




      