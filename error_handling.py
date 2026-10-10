try:
    a=int(input('Enter first Number: '))
    b=int(input('Enter second Number:'))
    print(a/b)
    
except ZeroDivisionError as z : 
    print('can not divide by zero',z)
    
except Exception as e:
    print('Somthing went wrong',e)
    
finally:
    print('BYE')