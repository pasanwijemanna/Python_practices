import array

arr = array.array('I',[2,3,4,5,6])

print(arr)

print(arr[0])

arr.append(8)
arr.insert(6,10)

print(arr)


arr.remove(10)
arr.pop(5)

print(arr)