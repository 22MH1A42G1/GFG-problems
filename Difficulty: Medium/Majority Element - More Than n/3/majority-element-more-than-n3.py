class Solution:
    def findMajority(self, arr):
        # code here
        first=second=None
        count_1=count_2=0
        for item in arr:
            if item==first:
                count_1+=1
            elif item==second:
                count_2+=1
            elif count_1==0:
                first=item
                count_1+=1
            elif count_2==0:
                second=item
                count_2+=1
            else:
                count_1-=1
                count_2-=1
        ans=[]
        for item in [first,second]:
            if arr.count(item)>len(arr)//3:
                ans.append(item)
        return sorted(ans)