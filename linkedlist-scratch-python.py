class Node:
    # constructor
    def __init__(self, data=None): 
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):  
        self.head = None
    
    def isEmpty(self):
        if(self.head == None):
            return True

    # insertion method for the linked list
    def push(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):            #finding the tail
                current = current.next
            current.next = newNode          #insert behind the tail
        
        else:
            self.head = newNode             #if no head, then its's our first node!
    
    def head_insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            newNode.next = current.next
            current.next = newNode
        else:
            self.head = newNode

    def insert(prevNode, data):
        if(prevNode == None):
            print("The given previous node is not valid")
            return data
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def delete(self, data):        
        if(self.head.data == data):
            queue_pop()
        
        prevNode = self.head
        current = prevNode.next
        while(current):
            if(current.data == data):
                prevNode.next = current.next
                current.next = None
                break
            prevNode = current
            current = current.next
        
        if(current == None):
            print("The given data is not here")

    def stack_pop(self):
        current = self.head
        prevNode = None
        while(current.next):
            prevNode = current
            current = current.next
        prevNode.next = None
        return current
    
    def queue_pop(self):
        temp = self.head
        self.head = self.head.next
        return temp

    # edit data
    def edit(node, newData):
        node.data = newData
    
    def edit_by_val(self, oldData, newData):
        current = self.head
        while(current):
            if(oldData == current.data):
                current.data = newData
                break
            current = current.next

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        print()

# Single Linked List with insertion and print methods
LL = SingleLinkedList()
LL.push(1)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(5)
LL.printLL()
LL.stack_pop()
LL.printLL()
LL.queue_pop()
LL.printLL()
LL.edit_by_val(3, 7)
LL.printLL()
LL.delete(7)
LL.printLL()