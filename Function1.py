# Function which accepts nothing and returns nothing
def Demo1():
    print("Inside Demo1")



# Function accepts one parameter and return nothing
def Demo2(No):
    print("Inside Demo2 with argument :",No)

# Function accepts one parameter and return one parameter
def Demo3(No):
    print("Inside Demo3 with argument",No)
    return No+2

# Function accepts two parameter and return one parameter
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    return Add

# Function  accepts two parameters and return two parameters
def Demo5(No1,No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2
    return  Add,Sub

def main():
    Demo1()

    Demo2(11)

    Ans = Demo3(10)
    print("Return value of Demo3 is : ",Ans)

    Ans = Demo4(10,11)
    print("Return value is :",Ans)

    Ans1,Ans2 = Demo5(11,10)
    print("First return value :",Ans1)
    print("Second return value :",Ans2)


if __name__=="__main__":
        main()
