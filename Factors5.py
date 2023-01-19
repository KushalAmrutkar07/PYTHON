# import NumberModule
# from NumberModule import DisplayFactors
# from NumberModule import *
import NumberModule as NUM

def main():
    print("Enter number : ")
    No = int(input())

    NUM.DisplayFactors(No)

if __name__=="__main__":
    main()

