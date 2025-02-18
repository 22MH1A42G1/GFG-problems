#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        def fun(x):
            return x[0]**2 + x[1]**2 
        points.sort(key=lambda x: fun(x))
        #print(points)
        return points[:k]
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends