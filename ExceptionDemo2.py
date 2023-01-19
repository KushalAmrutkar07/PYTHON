# Zero Error exception handle
def main():
    try:
        print("Enter first number")
        No1 = int(input())

        print("Enter second number")
        No2 = int(input())

    
        Ans = No1 / No2
        print("Division is :",Ans)   
    
    except ZeroDivisionError:
        print("Inside zero division error ")    

    except ValueError:
        print("Inside value error") 

    except Exception:  # generilised except block (MSD)
        print("Inside last except block")    

    finally: #destructor in c
        print("Inside finally block")       

if __name__ == "__main__":
    main()
        