class Solution:
    def majorityElement(self, arr):
        #code here
        n=len(arr)
        from collections import Counter
        c = Counter(arr)
        for i, j in c.items():
            if j > n//2:
                return i
        return -1