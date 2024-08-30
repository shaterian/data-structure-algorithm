class Graph:
    def __init__(self):
        self.adj_list = {}
    def print_graph(self):
        for vertex in self.adj_list:
            print(f'{vertex} : {self.adj_list[vertex]}')

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def exist_vertex(self, v):
        return v in self.adj_list.keys()
    
    
    def exist_edge(self, v1, v2):
        return (v1 in self.adj_list[v2] and v2 in self.adj_list[v1])

    def add_edge(self, v1 , v2):
        if v2 in self.adj_list.key() and v2 in self.adj_list.key():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if self.exist_vertex(v1) and self.exist_vertex(2) and self.exist_edge(v1, v2):
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, v):
        if self.exist_vertex(v):
            for n in self.adj_list[v]:
                self.adj_list[n].remove(v)
            del self.adj_list[v]
            return True
        return False
    
graph = Graph()
graph.add_vertex(1)
graph.print_graph()
