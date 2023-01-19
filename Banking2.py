# Instance Variable : Name,Amount,Address,AccountNumber
# Instance method : CreateAccount(),DisplayAccountInfo()
# Class Variable : Bank_Name,ROI_On_FD
# Class Method : DisplayBankInformation

class Bank_Account:

    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your Name :")
        self.Name = input()

        print("Enter your initial amount  :")
        self.Amount =int(input())    
    
        print("Enter your Address :")
        self.Address = input()    
    
        print("Enter your Account Number :")
        self.AccountNo = int(input())    
        
    def DisplayAccountInfo(self):
        print("-------Your Account information is below------")
        print("Name of Account Holder :",self.Name)
        print("Account Number :",self.AccountNo)  
        print("Address of Account Holder :",self.Address)
        print("Current Amount in Account :",self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is :",cls.Bank_Name)
        print("Rate of interst we offer on fixed deposite is :",cls.ROI_On_FD)


def main():
    print("Name of Bank :",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed deposit :",Bank_Account.ROI_On_FD)
    
    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()
    
    print("Creating the First Account")
    User1.CreateAccount()
    print("------------------------------------------------------------------------")
    
    print("Creating the Second Account") 
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()



if __name__=="__main__":
    main()    