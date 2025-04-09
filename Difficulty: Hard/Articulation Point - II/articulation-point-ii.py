class Solution:
    def articulationPoints(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        disc = [-1] * V   
        low = [-1] * V  
        parent = [-1] * V
        visited = [False] * V
        ap = [False] * V 
        time = [0]
        def dfs(u):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            children = 0
            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        for i in range(V):
            if not visited[i]:
                dfs(i)
        result = [i for i in range(V) if ap[i]]
        return result if result else [-1]



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends