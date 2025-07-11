class Solution:
    def countConsec(self, n: int) -> int:
        # code here 
        total = 2 ** n
        if n == 0:
            return 0 
        elif n == 1:
            return 0 
        a = 2  
        b = 3 
        for i in range(3, n + 1):
            a, b = b, a + b  
        no_consecutive_ones = b  
        return total - no_consecutive_ones
        