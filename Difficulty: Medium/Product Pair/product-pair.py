class Solution:
    def isProduct(self, arr, target):
        # code here
        from itertools import combinations
        n = len(arr)
        s = set()
        for i in arr:
            if i!=0 and target%i==0 and target//i in s:
                    return True
            s.add(i)
        return False