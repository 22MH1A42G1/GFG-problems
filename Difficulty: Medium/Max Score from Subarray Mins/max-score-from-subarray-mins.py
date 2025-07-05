class Solution:
    def maxSum(self, arr):
        # code here
        from itertools import pairwise
        return max(map(sum, pairwise(arr)))
    
