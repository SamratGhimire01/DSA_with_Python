class graph:
    def __init__(self,vertex):
        self.mul = [[0]*vertex for i in range(vertex)]
        self.size = vertex
    def insert(self,src,des):
        if not (0>= src <self.size and 0>= des <self.size):
            
        
            self.mul[src][des] = 1
            self.mul[des][src] = 1
            
            return "Done."
        return "Invalid range"
    
    def delete(self,src,des):
        if not (0>= src <self.size and 0>= des <self.size):
            
        
            self.mul[src][des] = 0
            self.mul[des][src] = 0
            
            return "Done."
        return "Invalid range"
        
    def printg(self):
        for row in self.mul:
            print(" ".join(map(str,row)))
        return
    
g=graph(5)
g.insert(2,3)
g.insert(1,2)
g.insert(3,4)
g.insert(4,1)

g.printg()


print('\n')

g.delete(3,4)

g.printg()