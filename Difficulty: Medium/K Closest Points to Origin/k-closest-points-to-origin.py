class Solution:
    def kClosest(self, points, k):
        # code here
        import heapq
        pq=[]
        for x,y in points:
            heapq.heappush(pq,(-x*x-y*y,x,y))
            if len(pq)>k:
                heapq.heappop(pq)
        return [(x,y) for _,x,y in pq]