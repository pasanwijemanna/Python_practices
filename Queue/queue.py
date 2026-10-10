class Queue:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        return str(self.list)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def enqueue(self,value):
        return self.list.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.list.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.list[0]
        
    def delete(self):
        self.list = None
        
        
myqueue = Queue()
print(myqueue.isEmpty())


myqueue.enqueue(2)
myqueue.enqueue(4)
myqueue.enqueue(6)
myqueue.enqueue(8)

print(myqueue)


myqueue.dequeue()
print(myqueue)

myqueue.dequeue()
print(myqueue)


print(myqueue.peek())

print(myqueue.delete())


