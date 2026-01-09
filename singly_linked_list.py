class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedlist:
    def __init__(self):
        self.head=None
    def insertatfirst(self):
        n=Node(int(input("Enter a number ")))
        n.next=self.head
        self.head=n
    def display(self):
        t=self.head
        if t==None:
            print("Nothing to print")
        else:
            while t!=None:
                print(t.data,end=" ")
                t=t.next
    def insertatend(self):
        if self.head==None:
            n=int(input("Enter a number: "))
            self.node=Node(n)
        else:
            t=self.head
            while t.next!=None:
                t=t.next
        t.next=Node(int(input("Enter a number ")))
    def deleteatfirst(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    def deletelast(self):
        if self.head==None:
            print("Nohting to delete")
        elif self.head.next==None:
            self.head==None
        else:
            t=self.head
            while t.next.next!=None:
                t=t.next
            t.next=None
    def countnode(self):
        t1=self.head
        if self.head==None:
            print("No node")
        else:
            count=0
            while t1!=None:
                t1=t1.next
                count+=1
            print(count)
    def sum(self):
        t1=self.head
        if self.head==None:
            print("No node")
        else:
            sum=0
            while t1!=None:
                sum+=t1.data
                t1=t1.next
            print(sum)
    def minval(self):
        t1=self.head
        if self.head==None:
            print("No node")
        else:
            min=self.head.data
            while t1!=None:
                if (t1.data<min):
                    min=t1
                else:
                    t1=t1.next
                
            print(min)

    def maxvall(self):
        t1=self.head
        if self.head==None:
            print("No node")
        else:
            max=self.head.data
            while t1!=None:
                if (max<t1.data):
                    max=t1.data
                else:
                    t1=t1.next  
            print(max)


        
    def evenno(self):
        t1=self.head
        if self.head==None:
            print("No node")
        else:
           while t1!=None:
               
            if(t1.data%2==0):
                   print(t1.data)
                
            t1=t1.next

    def oddno(self):
        t1=self.head
        if self.head==None:
            print("No node")
        else:
           while t1!=None:
               
            if(t1.data%2!=0):
                   print(t1.data)
                
            t1=t1.next

n1=SinglyLinkedlist()
n1.insertatfirst()
n1.insertatfirst()
n1.insertatend()
n1.insertatend()
n1.deleteatfirst()
n1.countnode()
n1.sum()
n1.minval()
n1.maxvall()
n1.evenno()
n1.oddno()
n1.display()