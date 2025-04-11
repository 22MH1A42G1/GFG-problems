class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        import heapq
        res = [0] * V
        q = [(0, src)]
        vis = set()
        adj = [[] for i in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        while len(vis) < V:
            w, v = heapq.heappop(q)
            if v in vis:
                continue
            res[v] = w
            vis.add(v)
            for u, uw in adj[v]:
                if u not in vis:
                      nw = w + uw
                      heapq.heappush(q, (nw, u))
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends