from functools import reduce

number = [1,2,3,4,5,6,7,8]

# def even_num(x):
#     return x % 2 == 0


# list1 = list(filter(even_num,number))

# print(list1)

list2 = list(filter(lambda x:x%2==0,number))
print(list2)



list3 = list(map(lambda x:x*2,number))
print(list3)


sum =reduce(lambda x,y : x+y,number)
print(sum)

