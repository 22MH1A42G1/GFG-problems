class Solution:
    def kokoEat(self, arr, k):
        # Code here
        import numpy as np
        arr = np.array(arr)
        low, high = 1, arr.max()
        ans = high
        while low <= high:
            mid = (low + high) // 2
            hours = np.sum(np.ceil(arr / mid))
            if hours <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

