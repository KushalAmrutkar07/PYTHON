from sys import *
import os
import hashlib
import time
#import schedule
import datetime


def DeleteFiles(dict1):
    results = list(filter(lambda x:len(x) > 1,dict1.values()))    
    icnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0    
    else:
        print("No duplicate files found.")

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb') # read Binary
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()    

def FindDup(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}   # Dictonary dups he arr madhe jayil main madhlya

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")

def PrintResults(dict1):
    results = list(filter(lambda x:len(x) > 1,dict1.values())) # filter

    if len(results) > 0:
        print("Duplicate Found :")

        print("The following files are identical.")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    print('\t\t%s' % subresult)
    else:
        print("No duplicate files found.")     

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    print ("Current time is:",datetime.datetime.now())

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of file")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        
        arr = {}  #Dictonary
        startTime = time.time()
        arr = FindDup(argv[1])
        PrintResults(arr)
        DeleteFiles(arr)
        endTime = time.time()
       
        print('Took %s seconds to evaluate.'%(endTime-startTime))
        
        #schedule.every(2).minutes.do(DeleteFiles())
        # while True:
            #schedule.run_pending()
            #time.sleep(1)

    except ValueError:
        print("Error : Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input",E)
if __name__ == "__main__":
    main()
