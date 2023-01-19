# User defined Decoration
def Hello():
    print("Inside Hello")

    def Demo():  # Inner function
        print("Inside Demo")
    
    Demo()

Hello()
       
        