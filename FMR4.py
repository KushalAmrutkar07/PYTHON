from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

Doubles = lambda No :  No*2

Sum = lambda A,B : A + B


def main():
    print("Enter number of elements of you want to enter :")
    iSize = int(input())

    Data_Input =[ ]
    print("please enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)

    Data_Filter = filter(CheckEven , Data_Input)
    print("Data after filter is :",Data_Filter)

    Data_Map = map(Doubles,Data_Filter)
    print("Data after map is :",Data_Map)

    Output = reduce(Sum,Data_Map)
    print("Result after reduce is : ",Output)


if __name__=="__main__":
    main()
