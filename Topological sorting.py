class Vertex:
    def __init__(self,name):
        self.name = name

class Graph:
    def __init__(self,size):
        self.size = size
        self.matrix = [[0]*size]*size
        self.vertices = {}

    def display_matrix(self):
        print("  ", end="")
        for num in range(self.size):
            print(str(num)+" ", end="")
        print()
        print("  ", end="")
        for num in range(self.size):
            print("--", end="")
        print()
        for ind,num in enumerate(self.matrix):
            print(str(ind)+"|",end="")
            for n in num:
                print(str(n)+" ",end='')
            print()

    def add_vertex(self,vertex):
        pass



v = Vertex("A")
g = Graph(10)
g.display()
