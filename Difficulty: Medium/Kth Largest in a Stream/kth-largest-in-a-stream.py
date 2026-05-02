class Solution:
    def kthLargest(self, arr, k):
        # code here 
        import heapq
        ans=[]
        st=[]
        for i in range(len(arr)):
            heapq.heappush(st,arr[i])
            if len(st)>k:heapq.heappop(st)
            if len(st)>=k:
                ans.append(st[0])
            else:
                ans.append(-1)
        return ans