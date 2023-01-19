#Accept number from user AND find the Minimum number fom the number

def Minimum(No1 , No2):
    if No1 < No2:
         return No1
    else:
         return No2

def main():
    print("Enter first number")
    Value1 = input()

    print("Enter second number")
    Value2 = input()

    Ans = Minimum(int(Value1), int(Value2))

    print("Smallest number is : ",Ans)

if __name__ == "__main__":
    main()

