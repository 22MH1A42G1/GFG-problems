class Solution:
    def findDuplicates(self, arr):
        # code here
        from collections import Counter
        c = Counter(arr)
        l =[]
        for i in c:
            if c[i]>1:
                l.append(i)
        return l
        