programming = {"C": "Ritchie", "C++": "Strousrup", "java" : "Gosling","Python": "Rossum"}

Batches = {"PPA": 18000,"LB":16700,"Python":16500,"Angular":15000}

print("____________________________")
print("Data of Dictonary :",Batches)

print("____________________________")

print("Data traversal using for loop")
for x in Batches:
    print(x)

print("_____________________________")
print("Data traversal using for loop")
for x in Batches:
    print(x,Batches[x])


print("_____________________________")
print("Data traversal using for loop")
for x in Batches:
    print(x,Batches.get(x))

print("____________________________")
keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)

print("____________________________")

