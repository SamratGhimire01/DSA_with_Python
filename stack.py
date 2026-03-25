class Stack:
    def __init__(self):
        self.l = []
    
    def length(self):
        return len(self.l)
    def push(self,value):
        self.l.insert(0,value)
    def peek(self):
        if len(self.l) == 0:
            raise Exception("Stack Empty.")
        return self.l[0]
    def pop(self):
        if len(self.l) == 0:
            raise Exception("Stack Empty.")
        return self.l.pop(0)

s= Stack()
s.push(30)
s.push(40)
s.push(50)
print(s.length())
print(s.peek())
print(s.pop())
print(s.pop())