# write a program in reverse order : 4,3,2,1 in Recurrsion

def Display(No):
    if(No > 0):
        print(No)
        No = No-1
        Display(No)

Display(4)     




        