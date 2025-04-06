class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        from collections import defaultdict
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        vis = [False]*V
        st = []
        def dfs(node):
            vis[node]=True
            for n in adj[node]:
                if not vis[n]:
                    dfs(n)
            st.append(node)
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return st[::-1]



#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, V, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends