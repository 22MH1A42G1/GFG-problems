class Solution:
	def tsp(self, cost):
		# code here
		n = len(cost)
        vis = (1 << n) - 1
        dp = [[float('inf')] * n for _ in range(1 << n)]
        dp[1][0] = 0  
        for i in range(1 << n):
            for u in range(n):
                if not (i & (1 << u)):
                    continue
                for v in range(n):
                    if i & (1 << v):
                        continue
                    j = i | (1 << v)
                    dp[j][v] = min(dp[j][v], dp[i][u] + cost[u][v])
        ans = float('inf')
        for i in range(n):
            ans = min(ans, dp[vis][i] + cost[i][0])
        return ans