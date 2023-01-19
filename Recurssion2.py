# ha Recurssion aahe pan ha thambat nahi aahe
# Recurssion
# display 4 times Hello in Screen

def Display(No):
    iCnt = 0
    if(iCnt < No):
        print("Hello")
        iCnt = iCnt+1
        Display(No)

Display(4)
        