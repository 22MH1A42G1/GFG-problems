class Solution:
    def findTwoElement(self, arr):
        # code here
        d=0
        from collections import Counter
        mp = Counter(arr)
        for i,j in mp.items():
            if j>1:
                d=i
        n = len(arr)
        r = ((n*(n+1))//2) - sum(set(arr))
        return [d,r]

