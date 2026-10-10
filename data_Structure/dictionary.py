dict1 = {
    "name" : 'pasan',
    "age"  : 20,
    "status" : 'in relationship',
    "Are you buy car " : True 
}

print(dict1)


print(dict1.keys())
print(dict1.values())
print(dict1.items())

for x,y in dict1.items():
    print(x,":",y)
    

dict1["education"] = "BSE undergraduate"
print(dict1)

dict1.update({'Gender':'Male'})
print(dict1)

dict1.pop("status")
print(dict1)

dict1.popitem()
print(dict1)


