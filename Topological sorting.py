import random


class Vertex:
    def __init__(self, name):
        self.name = name


class Graph:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for x in range(self.size)] for x in range(self.size)]
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
            print(str(ind)+"|", end="")
            for n in num:
                print(str(n)+" ", end='')
            print()
        print()

    def display(self):
        return self.matrix

    def add_edge(self,y,x):
        if self.matrix[y][x] == 0:
            self.matrix[y][x] = 1
            return True
        else:
            return False

    def show_edge(self,y,x):
        return self.matrix[y][x]

    def fill_graph(self,per):
        num_of_vertices = (self.size*(self.size-1)/2)*(per/100)
        for num in range(self.size - 1):
            self.add_edge(num, num+1)
            num_of_vertices -= 1
        while num_of_vertices > 0:
            y = random.randint(0,self.size-2)
            x = random.randint(y+1, self.size-1)
            if self.add_edge(y, x):
                num_of_vertices -= 1


v = Vertex("A")
g = Graph(10)
print(g.display())
g.display_matrix()
g.fill_graph(60)
g.display_matrix()
