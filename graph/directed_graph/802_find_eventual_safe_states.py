from typing import List
class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {} 

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = [] 
    
    def add_edge(self, start, next):
        if start not in self.adjacency_list:
            self.add_vertex(start)
        if next not in self.adjacency_list:
            self.add_vertex(next)

        self.adjacency_list[start].append(next) 
    
    def remove_edge(self,start, end):
        if start in self.adjacency_list and end in self.adjacency_list[start]:
            self.adjacency_list[start].remove(end) 

    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list:
            self.adjacency_list.pop(vertex)
        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                self.adjacency_list[v].remove(vertex)
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f" {vertex} -> {', '. join (map(str, edges))}")
    
    def get_neighbors(self,vertex):
        return self.adjacency_list.get(vertex,[]) 
    def has_edge(self,start, end):
        return end in self.adjacency_list.get(start,[])
    
dg = DirectedGraph()
dg.add_vertex(0)
dg.add_vertex(1)
dg.add_vertex(2)
dg.add_vertex(3)
dg.add_vertex(4)
dg.add_vertex(5)
dg.add_vertex(6)
dg.add_edge(0, 1)
dg.add_edge(0, 2)
dg.add_edge(1, 2)
dg.add_edge(2, 5)
dg.add_edge(3, 0)
dg.add_edge(4, 5)



print("Graph:")
dg.display()

print("\nNeighbors of 1:", dg.get_neighbors(1))
print("Edge exists from 1 to 2:", dg.has_edge(1, 2))
print("Edge exists from 3 to 2:", dg.has_edge(3, 2))

def eventualSafeNodes(graph):
    
    def dfs(node):
        if state[node] != 0:
            return state[node] == 2
        state[node] = 1 

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
            
        state[node]  = 2 
        
        return True 
    n = len(graph)

    state = [0] * n 

    print([node for node in range(n) if dfs(node)])

eventualSafeNodes(dg.adjacency_list)