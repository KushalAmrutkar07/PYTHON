# Accept 2 numbers and perform Addition and Substraction of it

# Kay karaycha aahe -> Behaviours (Functions)
# Addition ani Substraction

# Te karayla ky lagnar aahe  -> Characteristics (Data)
# 2 numbers

# Class = Characteristics + Behaviours
# Class = Data + Functions


class Arithematic:
    def  __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1 + self.No2


    def Sub(self):
        return self.No1 - self.No2


def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter Second number")
    Value2 = int(input())

    obj = Arithematic(Value1,Value2)

    Ans = obj.Add()   # 0X100.Add()
    print("Addition is :",Ans)

    Ans = obj.Sub()  # 0X100.Sub()
    print("Substraction is :",Ans)
if __name__=="__main__":
    main()