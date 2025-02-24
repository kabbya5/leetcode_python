from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list) 

        # **Step 1: Build the Tree Graph**
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # **Step 2: Find Bob's Path to Root (0)**
        def find_bob_path(node, parent):
            if node == 0:
                return [0]  # Bob reaches root
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    path = find_bob_path(neighbor, node)
                    if path:
                        return [node] + path  # Add current node to path
            
            return []
        
        bob_path = find_bob_path(bob, -1)  # Find path from Bob to root
        bob_time = {node: time for time, node in enumerate(bob_path)}  # Track Bob's arrival time

        # **Step 3: DFS to Calculate Maximum Profit**
        def dfs(node, parent, time):
            profit = 0
            if node in bob_time:
                if time < bob_time[node]:
                    profit = amount[node]  # Alice collects full amount
                elif time == bob_time[node]:
                    profit = amount[node] // 2  # Both reach at the same time, split profit
            else:
                profit = amount[node]  # Alice collects full amount
            
            is_leaf = True
            max_profit = float('-inf')

            for neighbor in graph[node]:
                if neighbor != parent:
                    is_leaf = False
                    max_profit = max(max_profit, dfs(neighbor, node, time + 1))

            return profit if is_leaf else profit + max_profit

        return dfs(0, -1, 0)  # Start DFS from root (0)

# **Test Case**
edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

s = Solution()
print(s.mostProfitablePath(edges, bob, amount))  # Output: 6
