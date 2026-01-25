class Solution:
    def permuteDist(self, arr):
        # code here
        
        n = len(arr)
        res = []

        def fun(arr, pos, n):
            if pos==n-1:
                res.append(arr[:])
                return

            for i in range(pos, n):
                arr[pos], arr[i] = arr[i], arr[pos]
                fun(arr, pos+1, n)
                arr[pos], arr[i] = arr[i], arr[pos]

        fun(arr, 0, n)
        return res
        