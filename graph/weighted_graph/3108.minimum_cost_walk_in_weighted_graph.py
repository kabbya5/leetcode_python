from collections import defaultdict 

def build_graphh(n,edges):
    graph = defaultdict(list) 
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w)) 
        return graph 
    

def minimum_cost_walk(n,edges, queries):
    graph = build_graphh(n, edges) 

    def bfs(start):
        min_cost = {i: -1 for i in range(n)}
        min_cost[start] = -1
        queue = [(start, -1)]

        while queue:
            node, cost = queue.pop(0) 
            for neighbor, weight in graph[node]:
                new_cost = cost & weight
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    queue.append((neighbor, new_cost))

        return min_cost 
    all_costs = {i: bfs(i) for i in range(n)}
    result = [] 
    for s, t in queries:
        result.append(all_costs[s].get(t, -1) if all_costs[s][t] != float('inf') else -1)
    return result


n = 4
edges = [[0, 1, 3], [1, 2, 5], [2, 3, 7], [0, 2, 6]]
queries = [[0, 3], [1, 2], [0, 1]]

print(minimum_cost_walk(n, edges, queries))