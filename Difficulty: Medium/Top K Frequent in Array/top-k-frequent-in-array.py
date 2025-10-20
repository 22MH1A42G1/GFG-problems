class Solution:
	def topKFreq(self, arr, k):
		# Code here
		freq=Counter(arr)
        sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return [num for num , _ in sorted_items[:k]]
		