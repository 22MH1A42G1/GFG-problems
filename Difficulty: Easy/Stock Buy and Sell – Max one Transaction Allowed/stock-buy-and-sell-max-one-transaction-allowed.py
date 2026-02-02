class Solution:
    def maxProfit(self, prices):
        # code here
        if not prices or len(prices) < 2:
            return 0
        mi = float('inf')  
        ma = 0  
        for p in prices:
            mi = min(mi, p)
            ma = max(ma, p - mi)
        return ma
