class Solution:
    def countLessEq(self, a, b):
        # code here
        from bisect import bisect_right
        b.sort()
        return [bisect_right(b, i) for i in a]