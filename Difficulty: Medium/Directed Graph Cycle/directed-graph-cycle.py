from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        # code here
        indeg = [0]*V
        adj = defaultdict(list)
        for i, j in edges:
            indeg[j] += 1
            adj[i].append(j)
        topo = []
        q = []
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        while(q):
            node = q.pop(0)
            topo.append(node)
            for it in adj[node]:
                indeg[it] -= 1
                if indeg[it] == 0:
                    q.append(it)
        return len(topo) != V

#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends