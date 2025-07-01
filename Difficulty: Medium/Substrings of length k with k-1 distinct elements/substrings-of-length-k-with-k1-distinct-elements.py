class Solution:
    def substrCount(self, s, k):
        # code here
        count = 0
        l = len(s)
        store = []
        for i in range(len(s)-(k-1)):
            store.append(s[i:i+k])
        # print(store)
        no = {}
        for x in store:
            for y in x:
                if y not in no:
                    no[y] = 1
                else:
                    no[y] += 1
            
            if len(no) == (k-1):
                count += 1
            no = {}
        return count