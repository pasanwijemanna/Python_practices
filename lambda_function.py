
area = lambda x : x * x 

print(area(5))



perimeter = lambda a,b : 2*a + 2*b

print(perimeter(4,5))




def apple(unit_price):
    return(lambda number_of_apples:number_of_apples*unit_price)

x=apple(40)
print(x(10))