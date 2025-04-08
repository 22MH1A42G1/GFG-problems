class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        graph = {i: [] for i in range(V)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Remove the edge (c, d) from the graph, since it's undirected remove both ends
        if d in graph[c]:
            graph[c].remove(d)
        if c in graph[d]:
            graph[d].remove(c)
        
        # Function to perform DFS from a given vertex
        def dfs(current, visited):
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        # Use DFS starting from c to find if d can be reached
        visited = set()
        dfs(c, visited)
        
        # If d is not reached from c then the edge (c, d) is a bridge
        return d not in visited


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends