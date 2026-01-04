class Solution:
    def sort012(self, arr):
        # code here
        z=arr.count(0)
        o=arr.count(1)
        t=arr.count(2)
        arr[:]=[0]*z+[1]*o+[2]*t
