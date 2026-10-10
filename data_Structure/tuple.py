tuple1 = ('doberman','richback','common','rota')

print(tuple1)

print(tuple1[0])

list1 = list(tuple1)

list1[0] = "pomenarian"

tuple1 = tuple(list1)

print(tuple1)

list1 = list(tuple1)

list1.remove("rota")

tuple2 = tuple(list1)

print(tuple2)
