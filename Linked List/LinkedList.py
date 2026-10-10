class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
class Singly:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # # Traversal operater type 01
    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next
            
    # Traversal operater  type 02  
    
        
    def print(self):
        if self.head is None:
            print("No Any values")
        else:
            node = self.head
            while node is not None:
                print(node.value,end=" ") 
                node = node.next
            print()
            
            
    # Insertion operater       
    def insert(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                    
    def search (self,searchValue):
        if self.head is None:
            print("Empty LinkedList")
        else:
            node = self.head
            while node is not None:
                if node.value == searchValue:
                    print("Value Found")
                    return
                node = node.next
            print("Value Not Found.")
            
    def delete(self,location):
        if location == 0 :
            if  self.head.next == self.tail.next:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == -1:
            if self.head.next == self.tail.next:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                       break
                    node = node.next
                node.next = None
                self.tail = node
        else:
            tempNode = self.head
            index = 0 
            while index < location -1 :
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next 
            if nextNode == self.tail:  
                self.tail = tempNode
            
            
             
              

linkedlist = Singly()
node1 = Node(4)
node2 = Node(9)


linkedlist.head = node1
node1.next = node2
linkedlist.tail = node2

# # Traversal operater type 01
# for node in linkedlist:
#     print(node.value , end = " ")

# Traversal operater type 02

linkedlist.print()

# Insertion operations

linkedlist.insert(6,0) # add begining

linkedlist.print()

linkedlist.insert(8,-1) # add end

linkedlist.print()

linkedlist.insert(10,1)  # add middle

linkedlist.print()


linkedlist.search(8)
linkedlist.search(100)



linkedlist.delete(0)  # delete begining

linkedlist.print()


linkedlist.delete(-1)  # delete end

linkedlist.print()


linkedlist.delete(2)  # delete middile

linkedlist.print()

