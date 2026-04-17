class graph:
    def __init__(self):
        self.adjlist = {}
    
    def adj_vertex(self,vertex):
        if not vertex in self.adjlist:
            self.adjlist[vertex] = []
    
    def insert(self,src,dest):
        self.adj_vertex(src)
        self.adj_vertex(dest)
        
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)
        
    def printg(self):
        for vertex in self.adjlist:
            print(vertex," -> " , self.adjlist[vertex])
            


g=graph()
g.insert(2,3)
g.insert(5,3)
g.insert(4,2)
g.insert(1,5)

g.printg()