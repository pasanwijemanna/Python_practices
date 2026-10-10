# x = open('file.txt','r')

# print(x.read())
# print(x.readline(),end="")
# print(x.readline())


# x.close()

with open('file.txt' ,'w') as Y:
    Y.write('1.IOT Engineer\n')
    Y.write('2.Robotics Engineer \n')

Y.close()


with open('file.txt','a') as a:
    a.write('3.AI Engineer')
    
a.close()
