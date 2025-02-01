
def findRedunantConnection(edges):

    def 
    n = len(edges) 
    uf = UnionFind(n + 1) 
    for u, v in edges:
        if not uf.union(u,v):
            return [u,v]
        
edges = [[1, 2], [1, 3], [2, 3]]

print(findRedundantConnection(edges))