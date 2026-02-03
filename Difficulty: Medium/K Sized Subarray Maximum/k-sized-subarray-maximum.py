class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        from collections import deque
        q, ans = deque(), []
        
        for i, e in enumerate(arr):
            while q and i-q[0]+1 > k:
                q.popleft()
            while q and arr[q[-1]] <= e:
                q.pop()
            q.append(i)
            if i >= k-1:
                ans.append(arr[q[0]])
        return ans