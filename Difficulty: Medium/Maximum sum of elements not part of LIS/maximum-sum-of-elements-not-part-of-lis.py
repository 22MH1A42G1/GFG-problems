class Solution:
    def nonLisMaxSum(self, arr):
        # code here
        from bisect import bisect_left
        n = len(arr)
        prev = [-1] * n
        total_sum = arr[0]
        lis = [0]
        for i in range(1, n):
            total_sum += arr[i]
            j = bisect_left(lis, arr[i], key=lambda k: arr[k])
            if j == 0:
                lis[0] = i
            else:
                prev[i] = lis[j - 1]
                if j == len(lis):
                    lis.append(i)
                else:
                    lis[j] = i
        lis_sum = 0
        i = lis[-1]
        while i != -1:
            lis_sum += arr[i]
            i = prev[i]
        return total_sum - lis_sum