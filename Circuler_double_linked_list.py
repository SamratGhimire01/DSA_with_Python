class Node:
    def __init__(self,value):
        self.data = value
        self.prev = None
        self.next = None
        
class DoublyLL:
    def __init__(self):
        
        self.head = None
    
    def insertAtEnd(self,value):
        temp = Node(value)
        
        if self.head is None:
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
            return
        t1 = self.head
        while (t1.next != self.head):
            t1 = t1.next
        if t1.next == self.head:
            temp.prev = t1
            t1.next = temp
            temp.next = self.head
            self.head.prev = temp
    def insertAtBeg(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.head.next = self.head
            self.head.prev = self.head
            return
        tail = self.head.prev
        
        temp.next = self.head
        temp.prev = tail
        self.head.prev = temp
        tail.next = temp
        self.head = temp
        
        
    def insertAtMiddle(self,value,x):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t1 = self.head
        while (t1.next != self.head):
            if t1.data == x:
                temp.next = t1.next
                temp.prev = t1
                t1.next.prev = temp
                t1.next = temp
                return
            t1 = t1.next
        if t1.data == x:
            temp.prev = t1
            temp.next = t1.next
            t1.next = temp
            return
        
    def deletell(self,x):
        if self.head.next == None and self.head.data == x:
            return
        if self.head.data == x:
            if self.head.next == self.head:
                self.head = None
            else:
                tail = self.head.prev
                self.head = self.head.next
                self.head.prev = tail
                tail.next = self.head
            return
                
            
        
        t1 = self.head
        while (t1.next != self.head):
            if t1.data == x:
                t1.next.prev = t1.prev
                t1.prev.next = t1.next
                return
            t1= t1.next
        if t1.data == x:
            t1.prev.next = self.head
            self.head.prev = t1.prev
            return


    def printl(self):
        t1 = self.head
        if t1:
            while (t1.next != self.head):
                print(t1.data, end = " <--> ")
                t1 = t1.next
            print(t1.data)
        else:
            print("empty list")
    
        
d=DoublyLL()
d.insertAtEnd(30)
d.insertAtEnd(50)
d.insertAtEnd(90)
d.insertAtBeg(5)
d.insertAtMiddle(22,90)
d.deletell(5)
d.printl()