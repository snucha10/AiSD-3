import random


class Vertex:
    def __init__(self, name):
        self.name = name


class Graph:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for x in range(self.size)] for x in range(self.size)]
        self.vertices = {}
        self.graph = {}

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

    def topological_sort(self):
        visited = [0]*self.size
        tp_sorted = []
        while 0 in visited:
            idx = visited.index(0)
            self.ts(idx,visited,tp_sorted)
        return tp_sorted[::-1]



    def ts(self,v,visited,tp_sorted):
        visited[v]=1
        for num in range(self.size):
            if visited[num]==0 and self.matrix[v][num]==1:
                self.ts(num, visited, tp_sorted)
        tp_sorted.append(v)


v = Vertex("A")
g = Graph(11)
g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(1, 5)
g.add_edge(2, 6)
g.add_edge(2, 9)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(4, 2)
g.add_edge(6, 7)
g.add_edge(8, 1)
g.add_edge(8, 9)
g.add_edge(8, 2)
g.add_edge(10, 3)
g.add_edge(10, 8)
g.display_matrix()
print(g.topological_sort())
