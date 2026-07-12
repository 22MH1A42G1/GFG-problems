class Solution:
    def maxAmount(self, arr, k):
        # code here
        import heapq
        mod = 10**9+7
        heap = [-x for x in arr]
        heapq.heapify(heap)
        ans = 0
        while k>0 and heap:
            cur = -heapq.heappop(heap)
            ans = (ans+cur)%mod
            if cur > 1:
                heapq.heappush(heap, -(cur-1))
            k-=1
        return ans