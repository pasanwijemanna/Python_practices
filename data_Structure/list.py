friuts = ['Apple','Cherry','Banana','Kivi']

print(friuts[2])
print(friuts[0:2])
print(friuts[-1])

friuts[-1] = "melon"

friuts.append("DragonFriuts")

friuts.insert(0,"rose")

print(friuts)


friuts.pop()
friuts.remove("rose")

print(friuts)

vegitables =['carrots','Batana','pumkin','leeks']

friuts.extend(vegitables)
print(friuts)

print (len(friuts))

sh = [x if x[0]== "B" else "not matching" for x in friuts]
sc = [x for x in friuts ]
print(sh)
print(sc)

friuts.sort()
print(friuts)


x = 0
while x < len(friuts):
    print(friuts[x])
    x += 1
