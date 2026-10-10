class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        return str(self.list)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self,value):
        return self.list.append(value)    

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[-1]
        
    def delete(self):
        #self.list.clear()
        self.list = None

myStack = Stack()
print(myStack.isEmpty())


myStack.push(2)  # add a Element
myStack.push(4)
myStack.push(6)
myStack.push(8)


print(myStack)


myStack.pop()  # delete a last element
print(myStack)


print(myStack.peek()) # return a last element



myStack.delete()
print(myStack) # delete all Element




