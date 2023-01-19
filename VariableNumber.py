

def Add(*Values):
    Sum = 0
    for no in Values:
        Sum = Sum + no

    return Sum



def AddX(*Values):
    Sum = 0
    for i in range(0,len(Values),1):
        Sum = Sum + Values[i]

    return Sum

def main():
    Ans = 0
    Ans = Add(10,11,6,5,9,4)
    print("Addition is ",Ans)





if __name__=="__main__":
    main()