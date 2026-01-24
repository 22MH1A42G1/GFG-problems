class Solution:
    def josephus(self, n, k):
        # code here
        nxt=[*range(1,n)]+[0]
        prv=[n-1]+[*range(n-1)]
        cur=-1
        while nxt[cur]!=cur:
            for _ in range(k):
                cur=nxt[cur]
            nxt[prv[cur]]=nxt[cur]
            prv[nxt[cur]]=prv[cur]
        return cur+1