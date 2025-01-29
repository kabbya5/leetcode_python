class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {} 

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex]  = []

    def add_edge(self, vertex, edge):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = [] 
        self.adjacency_list[vertex].append(edge)

    def remove_edge(self, vertex, edge):
        if vertex in self.adjacency_list and edge in self.adjacency_list[vertex]:
            self.adjacency_list[vertex].remove(edge)
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex] 

        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                self.adjacency_list[v].remove(vertex)
    
    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")
    
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex,[])
    
    def has_edge(self, start, end):
        return end in self.adjacency_list.get(start, [])
    
    def checkIfPrerequisite(self,n, prerequisites, queries):
        reach = [[False] * n for _in range(n)]
        
        for u, v in prerequisites:
            reach[u][v] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        
        return [reach[u][v] for u, v in queries]
    

if __name__ == "__main__":
    graph = DirectedGraph()
    graph.add_edge("0", "1")
   
    print("Directed Graph:")
    graph.display()

   

    

# Example Usage
n = 2
prerequisites = [(0, 1)]
queries = [[0,1],[1,0]]
print(graph.checkIfPrerequisite(n, prerequisites, queries))