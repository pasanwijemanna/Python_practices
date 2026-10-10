def test(a):
    for i in a:
        yield i
    


y = test([2,4,6,8])

print(next(y))
print(next(y))
print(next(y))
print(next(y))



print ('fibonacci')

def fib():
    a,b = 0,1
    while True:
        c = a+b
        yield a 
        a,b = b,c
        
y = fib()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))