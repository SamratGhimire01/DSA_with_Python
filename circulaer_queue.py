class Stack:
    def __init__(self):
        self.l = [0]*7
        print(self.l)
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def length(self):
        return self.count
    def enqueue(self,value):
        if self.count == 7:
            print("Overflow!.")
        self.l[self.rear] =value
        self.rear = (self.rear +1)%7
        self.count +=1
    def peek(self):
        if self.count == 0:
            print("UnderFlow!")
        return self.l[self.front]
    def dequeue(self):
        if self.count == 0:
            print("UnderFlow!")
        val = self.l[self.front]
        self.l[self.front] = 0
        self.front = (self.front+1)%7
        self.count-=1

        return val

s= Stack()
s.enqueue(30)
s.enqueue(40)
s.enqueue(50)
print(s.length())
print(s.peek())
print(s.dequeue())
print(s.dequeue())  


