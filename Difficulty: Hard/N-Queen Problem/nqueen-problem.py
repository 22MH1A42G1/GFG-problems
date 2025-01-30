#User function Template for python3

class Solution:
    def nQueen(self, n):
        result = []
        def backtrack(col, path, rows, diags, anti_diags):
            if col > n:
                result.append(path)
                return
            for row in range(1, n+1):
                row_mask = 1 << (row - 1)
                diag = row - col
                diag_mask = 1 << (diag + n - 1)
                anti_diag = row + col
                anti_diag_mask = 1 << (anti_diag - 2)
                if not (rows & row_mask) and not (diags & diag_mask) and not (anti_diags & anti_diag_mask):
                    backtrack(col + 1, path + [row], rows | row_mask, diags | diag_mask, anti_diags | anti_diag_mask)
        backtrack(1, [], 0, 0, 0)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends