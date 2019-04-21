import random
from KlasyPomocnicze.ListaP import LinkedList


class GraphMatrix:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for x in range(self.size)] for x in range(self.size)]
        self.vertices = []
        self.edges = {}

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

    def add_vertex(self,x):
        self.vertices.append(x)

    def add_edge(self, y, x):
        if y in self.vertices and x in self.vertices and self.matrix[y][x] == 0:
            self.matrix[y][x] = 1
            self.edges[y] = x
            return True
        else:
            return False

    def show_edge(self, y, x):
        return self.matrix[y][x]

    def fill_graph(self,per):
        num_of_vertices = (self.size*(self.size-1)/2)*(per/100)
        for num in range(self.size - 1):
            self.add_edge(num, num+1)
            num_of_vertices -= 1
        while num_of_vertices > 0:
            y = random.randint(0, self.size-2)
            x = random.randint(y+1, self.size-1)
            if self.add_edge(y, x):
                num_of_vertices -= 1

    def topological_sort(self):
        tp_sorted = []
        visited = {}
        for el in self.vertices:
            visited[el] = 0
        while 0 in visited.values():
            for el in visited.keys():
                if visited[el] == 0:
                    idx = el
                    break
            self.ts(idx, visited, tp_sorted)
        return tp_sorted

    def ts(self, v, visited, tp_sorted):
        visited[v]=1
        for num in self.vertices:
            if visited[num] == 0 and self.matrix[v][num] == 1:
                self.ts(num, visited, tp_sorted)
        tp_sorted.insert(0, v)


class GraphList:

    def __init__(self):
        self.lst = []
        self.vertices = []

    def add_vertex(self,x):
        if x not in self.vertices:
            self.vertices.append(x) # dodanie nowego wierzchołka do listy wierzchołków
            self.vertices.sort()

            element = LinkedList() # dodanie wierzchołka z ktrórego wychodzi dana krawędź
            self.lst.append(element)
            element.append(x)

    def add_edge(self, y, x):
        if y in self.vertices and x in self.vertices:
            for el in self.lst:
                first_el = el.head.next
                if first_el.value == y:
                    el.append(x)
                    break

    def display(self):
        for el in self.lst:
            print(el.display())

    def topological_sort(self):
        visited = {}
        tp_sorted = []
        for el in self.vertices:
            visited[el] = 0
        while 0 in visited.values():
            for e in self.lst:
                if visited[e.head.next.value] == 0:
                    self.ts(e.head.next, visited, tp_sorted)
        return tp_sorted

    def ts(self, v, visited, tp_sorted):
        #print(visited, tp_sorted, v.value)
        visited[v.value] = 1
        value = v.value
        while True:
            #print(visited, tp_sorted, v.value)
            if v.next is not None:
                #print(visited[v.next.value])
                if visited[v.next.value] == 0:
                    v = v.next
                    v = self.lst[v.value].head.next  #
                    self.ts(v, visited, tp_sorted)
                else:
                    v = v.next
            else:
                break

        #print(visited, tp_sorted, v.value)
        tp_sorted.insert(0, value)


gl = GraphList()
gl.add_vertex(0)
gl.add_vertex(1)
gl.add_vertex(2)
gl.add_vertex(3)
gl.add_vertex(4)
gl.add_vertex(5)
gl.add_vertex(6)
gl.add_vertex(7)
gl.add_vertex(8)
gl.add_vertex(9)
gl.add_vertex(10)
gl.add_vertex(11)
gl.add_edge(5, 11)
gl.add_edge(11, 2)
gl.add_edge(11, 9)
gl.add_edge(11, 10)
gl.add_edge(7, 11)
gl.add_edge(7, 8)
gl.add_edge(8, 9)
gl.add_edge(3, 8)
gl.add_edge(3, 10)
gl.display()
print(gl.vertices)
print(gl.topological_sort())
# g = GraphMatrix(12)
# g.add_vertex(5)
# g.add_vertex(7)
# g.add_vertex(3)
# g.add_vertex(11)
# g.add_vertex(8)
# g.add_vertex(2)
# g.add_vertex(9)
# g.add_vertex(10)
# g.add_edge(5, 11)
# g.add_edge(11, 2)
# g.add_edge(11, 10)
# g.add_edge(11, 9)
# g.add_edge(7, 11)
# g.add_edge(7, 8)
# g.add_edge(8, 9)
# g.add_edge(3, 8)
# g.add_edge(3, 10)
# g.display_matrix()
# print(g.topological_sort())
