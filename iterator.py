lst = {3,5,6}

itr = iter(lst)

# print(next(itr))
# print(next(itr))

while True:
    try:
        print(next(itr))
    except StopIteration:
        break
    
print('custom iterator')
   
# custom iterator

class myit:
    def __init__(self):
        self.y=2
    def __iter__(self):
        return self
    def __next__(self):
        val = self.y
        self.y += 2
        return val

myobj = myit()
itr = iter(myobj)
print(next(itr))
print(next(itr))

