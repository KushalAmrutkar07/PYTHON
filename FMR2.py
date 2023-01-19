def CheckEven(No):   # 1
    return (No % 2 == 0)

def Doubles(No):   # 2
    return  No*2

def Sum(A,B):   # 3
    return A + B

def filterX(Helper_Function,Data):  # 1
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)

    return Result

def mapX(Helper_Function,Data):            # 2
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)

    return Result

def reduceX(Helper_Function,Data):     # 3
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,no)

    return Ans

def main():
    print("Enter number of elements of you want to enter :")
    iSize = int(input())

    Data_Input =[ ]
    print("please enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)

    Data_Filter = filterX(CheckEven , Data_Input)
    print("Data after filter is :",Data_Filter)

    Data_Map = mapX(Doubles,Data_Filter)
    print("Data after map is :",Data_Map)

    Output = reduceX(Sum,Data_Map)
    print("Result after reduce is : ",Output)


if __name__=="__main__":
    main()
