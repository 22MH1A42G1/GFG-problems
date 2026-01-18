class Solution:
    def nextFreqGreater(self, arr):
        # code here
        n = len(arr)
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        res = [-1] * n
        st = []
        for i in range(n):
            while st and freq[arr[i]] > freq[arr[st[-1]]]:
                res[st.pop()] = arr[i]
            st.append(i)
        return res