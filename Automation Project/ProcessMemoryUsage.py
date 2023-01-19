import psutil

def ProcessDisplay():
    listprocess =[]

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024 * 1024) #Vms : Virtual memory size

            listprocess.append(pinfo);
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess    

def main():
    print("Marvellous Infosystems :Python Automation & Machine Learning")

    print("Process Monitor with memory usage")

    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)
    

if __name__ =="__main__":
    main()    
  



      