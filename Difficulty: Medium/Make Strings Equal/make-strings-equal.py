class Solution:
    def minCost(self, s, t, transform, cost):
        # code here
        INF = 10**12
        dist = [[INF] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        for i, (x, y) in enumerate(transform):
            u = ord(x) - ord('a')
            v = ord(y) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        ans = 0
        for i in range(len(s)):
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            if a == b:
                continue
            best = INF
            for c in range(26):
                if dist[a][c] < INF and dist[b][c] < INF:
                    best = min(best, dist[a][c] + dist[b][c])
            if best == INF:
                return -1
            ans += best
        return ans