# Normal functions / Named Functions
# def Function_Name(Function_Parameters):
# Function_Body
def Add(No1,No2):
    return  No1 + No2


# Lambda Functions / Unnamed Functions
# Lambda parameters : body

AddFunction = lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function :",Ans1)
print("Addition using lambda function :",Ans2)

print("Type of lambda function is :",type(AddFunction))