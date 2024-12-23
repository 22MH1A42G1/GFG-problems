class Solution:
    # Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            # Binary search on the i-th row
            l, h = 0, n - 1
            if mat[i][l] <= x <= mat[i][h]:
                while l <= h:
                    mid = (l + h) // 2
                    if mat[i][mid] == x:
                        return 1
                    elif mat[i][mid] < x:
                        l = mid + 1
                    else:
                        h = mid - 1
        return 0




#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends