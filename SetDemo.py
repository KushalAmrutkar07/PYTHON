print("Demonstration of Set")


# Data : Heterogeneous
#Orderd : No
# Indexed : No
# Mutable : Yes
#Duplicates : No


data = {11,21,51,101,21,11}   #Duplicates
data1 = {11,90.80,True,"Hello"}   # Heterogeneous

print("First set data :",data)
print("Length of data:",len(data))
print("Data is Heterogeneous :",data1)
print("Data is unordered :",data1)
# print("Data at index 2 : ",data1[2])
print("Data with unique elements :",data)


print("Set is mutable")
# Insert element in set
data.add(211)
print("Data after insertion :",data)

#Remove element
data.remove(211)
print("Data after removal :",data)

data.discard(201)
print("Data after discard :",data)