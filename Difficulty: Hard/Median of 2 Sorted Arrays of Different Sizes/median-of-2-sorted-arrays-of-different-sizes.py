#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        c = sorted(a+b)
        n = len(c)
        if n % 2 == 1:
            return c[n // 2]
        else:
            m1 = c[ n // 2 - 1]
            m2 = c[ n // 2]
            return (m1 + m2) / 2