class Solution:
    def searchMatrix(self, mat, x):
        # code here
        for i in mat:
            if x in i:
                return True
                
        return False