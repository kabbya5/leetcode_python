from collections import defaultdict 

def countCompleteComponents(n,edges):
    graph = defaultdict(set)

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    visited = set()
    complete_count = 0 

    def dfs(node, component):
        visited.add(node)
        component.append(node)
    
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor,component)
            
        
    for node in range(n):
        if node not in visited:
            component = []
            dfs(node,component)

            size = len(component)
            expected_edges = size * (size - 1) // 2 
            actual_edges = sum(len(graph[node]) for node in component) // 2

            if actual_edges == expected_edges:
                complete_count += 1 

    return complete_count


n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
print(countCompleteComponents(n, edges))