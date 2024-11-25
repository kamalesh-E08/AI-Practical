class Graph:
    def __init__ (self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges: self.adjList[src].append(dest)
        self.adjList[dest].append(src)

def DFS(graph, v, discovered):
    discovered[v] = True 
    print(v, end='')
    for u in graph.adjList[v]: 
        if not discovered[u]:
            DFS(graph, u, discovered)

if  __name__ == "__main__":
    edges = [(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4), (3, 5), (8, 9), (8, 12), (9, 10), (9, 11) ]
    n=13
    graph=Graph(edges, n)
    discovered = [False]*n
    for i in range(n):
        if not discovered[i]: DFS(graph, i, discovered)