class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self):
        n=Node(int(input("Enter a number ")))
        n.next=self.head
        self.head=n
    def pop(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    def enqueue(self):
        n=Node(int(input('Enter a data to insert at end ')))
        t=self.head
        if t==None:
            self.head = n
        else:
            while t.next!=None:
                t=t.next
            t.next=n
            
    def dequeue(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None    
    def display(self):
        t=self.head
        if self.head == None:
            print("Nothing to print")
        else:
            while t!=None:
                print(t.data)
                t=t.next
    def printpeak(self):
        if self.head==None:
            print("Nothing to print")
        else:
            print(self.head.data)
    def printqueuefirst(self):
        if self.head==None:
            print("Nothing at peak")
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            print(t.data)
                
                
    
            
n1=Stack()
# n1.push()
# n1.push() 
# n1.push()
# n1.push()
# n1.pop()
n1.enqueue()
n1.enqueue()
n1.enqueue()
n1.display()
# n1.printpeak()
n1.printqueuefirst()

