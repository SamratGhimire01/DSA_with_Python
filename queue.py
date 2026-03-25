
class Stack:
    def __init__(self):
        self.l = []
        self.front = 0
        self.rear = 0
    
    def length(self):
        return len(self.l)
    def enqueue(self,value):
        self.l.append(value)
        self.rear +=1
    def peek(self):
        if len(self.l) == 0:
            raise Exception("Stack Empty.")
        return self.l[self.front]
    def dequeue(self):
        if len(self.l) == 0:
            raise Exception("Stack Empty.")
        dequeues = self.l.pop(self.front)
        self.rear-=1
        return dequeues

s= Stack()
s.enqueue(30)
s.enqueue(40)
s.enqueue(50)
print(s.length())
print(s.peek())
print(s.dequeue())
print(s.dequeue())