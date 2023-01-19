# Write file
import os

def Write_File(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write in the file")
        Data = input()
        
        fd = open(FileName,"a") # a = append
        fd.write(Data)
    else:
        print("File is not existing")
        return    

def main():
    print("Enter the file name to Write")
    Name = input()

    Write_File(Name)

if __name__=="__main__":
    main()
  



      