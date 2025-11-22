class Solution:
    def minConnect(self, V, edges):
        # code here
        from collections import defaultdict 
        def dfs(n,v,g):
            v[n]=1
            for i in g[n]:
                if not v[i]:
                    dfs(i,v,g)
        E = len(edges)
        if E<V-1: return -1
        g = defaultdict(list)
        for r,c in edges:
            g[r].append(c)
            g[c].append(r)
        ans = 0
        v = [0]*V
        for i in range(V):
            if not v[i]:
                dfs(i,v,g)
                ans+=1
        return ans-1
