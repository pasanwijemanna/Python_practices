class BSTNode:
    def __init__(self,data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None
        
        
def insert(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insert(rootNode.leftChild , nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insert(rootNode.rightChild , nodeValue)
    return "Node Inserted."
        

#Traversal operations

def preOderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data , end =" ")
    preOderTraversal(rootNode.leftChild)
    preOderTraversal(rootNode.rightChild)           

def inOderTraversal(rootNode):
    if not rootNode:
        return
    inOderTraversal(rootNode.leftChild)
    print(rootNode.data , end =" ")
    inOderTraversal(rootNode.rightChild)    
    
def postOderTraversal(rootNode):
    if not rootNode:
        return
    postOderTraversal(rootNode.leftChild)
    postOderTraversal(rootNode.rightChild)
    print(rootNode.data , end =" ")   
    
# search operations

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print("Found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None:
            if rootNode.leftChild == nodeValue:
                print("Found")
            else:
                searchNode(rootNode.leftChild,nodeValue)
        else:
            print("Not Found.")    
    else:
        if rootNode.rightChild is not None:
            if rootNode.rightChild == nodeValue:
                print("Found")
            else:
                searchNode(rootNode.rightChild,nodeValue)
        else:
            print("Not Found.")        

# searching minimum value
def minvalNode(BSTNode):
    current = BSTNode
    while(current.leftChild is not None):
        current = current.leftchild
    return current


# Delete operations

def delete(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = delete(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = delete(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode =None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode =None
            return temp
        
        temp = minvalNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild =delete(rootNode.rightChild,temp.data)
    return rootNode
        
newBST = BSTNode(6)

print(insert(newBST,4))
print(insert(newBST,8))
print(insert(newBST,2))
print(insert(newBST,5))
print(insert(newBST,9))
print(insert(newBST,1))

preOderTraversal(newBST)
print()
inOderTraversal(newBST)
print()
postOderTraversal(newBST)
print()

searchNode(newBST,9)
searchNode(newBST,20)
         
        