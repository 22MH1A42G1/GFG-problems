class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
        if image[sr][sc] == newColor:
	        return image
	    
		self.dfs(image, sr, sc, image[sr][sc], newColor)
		return image
	
	def dfs(self, image, x, y, currColor, newColor):
	    if x < 0 or y < 0 or x == len(image) or y == len(image[0]) or image[x][y] != currColor:
	        return
	   
	    image[x][y] = newColor
	    self.dfs(image, x + 1, y, currColor, newColor)
	    self.dfs(image, x - 1, y, currColor, newColor)
	    self.dfs(image, x, y + 1, currColor, newColor)
	    self.dfs(image, x, y - 1, currColor, newColor)


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends