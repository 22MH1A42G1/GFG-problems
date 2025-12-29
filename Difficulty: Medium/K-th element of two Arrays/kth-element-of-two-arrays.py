class Solution:
    def kthElement(self, a, b, k):
        # code here
        arr=a+b
        arr.sort()
        return arr[k-1]