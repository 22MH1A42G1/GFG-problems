class Solution:
    def utility(self, a, b, opr):
        # code here
        if opr == 1:
            print (a+b)
        elif opr==2:
            print(a-b)
        elif opr==3:
            print(a*b)
        else:
            print("Invalid Input")