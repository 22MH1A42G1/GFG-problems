class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n = len(arr)
        for i in range(n):
            if arr[i] <= k:
                arr[i] = -1
            else:
                arr[i] = 1
        
        prefixSum = {}
        currSum = 0
        maxLen = 0

        for i, num in enumerate(arr):
            currSum += num
            
            if currSum > 0:
                maxLen = i+1
            
            
            if currSum - 1 in prefixSum:
                maxLen = max(maxLen, i - prefixSum[currSum - 1])
            
            if currSum not in prefixSum:
                prefixSum[currSum] = i
        
        return maxLen