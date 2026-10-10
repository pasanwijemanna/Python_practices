from array import * 
arr = array('i',[4,3,2,6,8])
print(arr)

# Insert element to array

arr.append(100)
print(arr)

arr.insert(0,999)
print(arr)

arr.extend([10,20,30,40,50])
print(arr)


# Traveral operation

for i in arr:    
    print(i)
    

# Access array elements

print(arr[0])
print(arr[5])  


# Deleting an element

arr.remove(999)
print(arr)

arr.pop()
print(arr)