class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLL:
    def __init__(self,head=None):
        self.head=head
    
    def insertAtEnd(self,value):
        temp = Node(value)
        t1=self.head
        if t1 == None:
            self.head = temp
            return
        while (t1.next != None):
             t1= t1.next
        t1.next = temp
        
    def insertAtBeg(self,value):
        temp = Node(value)
        if self.head is None:
            self.head= temp
            return
        temp.next = self.head
        self.head = temp
        
    def insertAtMiddle(self,value,x):
        temp = Node(value)
        if self.head.data == x:
            temp.next = self.head.next
            sef.head.next = temp
            return
        t1= self.head
        while(t1.next != None):
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                return
            t1=t1.next
        
    def deletes(self,x):
        if self.head.data == x:
            temp = self.head.next
            self.head = temp
        
        t1 = self.head
        prev = t1
        while t1.next != None:
            if t1.data == x:
                prev.next = t1.next
                return
            else:
                prev = t1
                t1= t1.next
        if t1.data == x:
            prev.next = None
    
    def printsee(self):
        t1=self.head
        while(t1.next != None):
            print(t1.data)
            t1= t1.next
        print(t1.data)

s = SinglyLL()
s.insertAtEnd(10)
s.insertAtEnd(20)
s.insertAtEnd(30)
s.insertAtBeg(5)
s.insertAtBeg(11)
s.insertAtMiddle(55,30)
s.deletes(30)
s.printsee()
    