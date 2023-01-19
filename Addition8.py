print("Application to demonstrate Industrial programming")

import MarvellousModule

def main():
    print("Value of__name__from main is : ",__name__)

    print("Enter first number : ")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    Ret = MarvellousModule. Addition(no1,no2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()

