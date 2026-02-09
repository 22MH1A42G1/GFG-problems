class Solution:
    def findKRotation(self, arr):
        # code here
        sa = sorted(arr)
        # print(sa)
        for i in range(len(arr)):
            if sa[0] == arr[i]:
                return i
        