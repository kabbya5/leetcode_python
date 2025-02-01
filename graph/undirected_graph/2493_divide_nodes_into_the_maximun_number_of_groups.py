from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def bfs(start):
            queue = deque([start])
            dist = {start: 1}
            max_level = 1
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        max_level = max(max_level, dist[neighbor])
                        queue.append(neighbor)
                    elif (dist[neighbor] - dist[node]) % 2 == 0:
                        return -1  
        
            return max_level

        visited = set()
        result = 0  
        for node in range(1, n + 1):
            if node not in visited:
                component_nodes = [] 
                queue = deque([node])
                
                while queue:
                    curr = queue.popleft() 
                    if curr in visited:
                        continue 
                    visited.add(curr) 
                    component_nodes.append(curr) 

                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        
                max_depth = 0  
                for start in component_nodes:
                    depth = bfs(start) 
                    if depth == -1:
                        return -1  
                    max_depth = max(max_depth, depth)

                result += max_depth  

        return result 


# টেস্ট
s = Solution() 
n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
print(s.magnificentSets(n, edges))  
