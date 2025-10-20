from math import factorial

class Solution:
    def catalan_number(self,n):
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))
    def countBSTs(self, arr):
        # Code here
        result = []
        for root in arr:
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            left_count = self.catalan_number(len(left))
            right_count = self.catalan_number(len(right))
            result.append(left_count * right_count)
        return result