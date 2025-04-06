#User function Template for python3

class Solution:
    def isSafe(self, i, j, n, m):
        return (0 <= i < n) and (0 <= j < m)
        
    def dfs(self, p, vis, n, m):
        dirs = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
        for dx, dy in dirs:
            x, y = p[0] + dx, p[1] + dy
            if self.isSafe(x, y, n, m) and not vis[x][y]:
                vis[x][y] = True
                self.dfs((x, y), vis, n, m)

    def numIslands(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'W':
                    vis[i][j] = True
        
        count = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j]:
                    count += 1
                    self.dfs((i, j), vis, n, m)
            
        return count

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends