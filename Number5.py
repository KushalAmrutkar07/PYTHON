# POP to OOP -> Accept N number from user and return Minimum of that number of that Number

class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()

    def Accept(self):
        print("Enter how many elements you want :")
        self.Size = int(input())

        print("Please enter the elements")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
      print("Elements from list are :")
      for i in range(0,self.Size):
         print(self.Arr[i])

    def Minimum(self):
       Min = self.Arr[0]

       for i in range(0,self.Size):

          if(self.Arr[i] < Min):
              Min = self.Arr[i]

       return Min

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Minimum()
    print("Minimum of all elements is :",Output)
if __name__ == "__main__":
    main()

        