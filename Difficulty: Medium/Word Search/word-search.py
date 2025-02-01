class Solution:
    def isWordExist(self, mat, word):
        def dfs(i, j, k):
            if k == len(word): return True
            if not (0<=i<len(mat) and 0<=j<len(mat[0]) and mat[i][j]==word[k]): return False
            mat[i][j], tmp = '#', mat[i][j]
            res = any(dfs(i+di,j+dj,k+1) for di,dj in [(-1,0),(1,0),(0,-1),(0,1)])
            mat[i][j] = tmp
            return res
        return any(dfs(i,j,0) for i in range(len(mat)) for j in range(len(mat[0])))


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends