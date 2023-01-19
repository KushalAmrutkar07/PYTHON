# using while loop same question


def main():
    print("Enter number : ")
    No = int(input())


    i = 1;
    print("Factors are : ")
    while(i <= (No/2)):
        if ((No % i) ==0):

          print(i)
        i  = i+1


if __name__=="__main__":
    main()