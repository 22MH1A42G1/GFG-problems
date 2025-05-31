class Solution:
	def countPairs(self, mat1, mat2, x):
		# code here
	    arr1 = [j for i in mat1 for j in i]
	    arr2 = [j for i in mat2 for j in i]
        
        arr1.sort()
        arr2.sort()

        i = 0
        j = len(arr2) - 1
        count = 0

        while i < len(arr1) and j >= 0:
            total = arr1[i] + arr2[j]
            if total == x:
                count += 1
                i += 1
                j -= 1
            elif total < x:
                i += 1
            else:
                j -= 1

        return count
