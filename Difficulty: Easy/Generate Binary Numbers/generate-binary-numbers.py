class Solution:
    def generateBinary(self, n):
        # code here
        q = deque()
        q.append("1")
        res = []
        for _ in range(n):
            curr = q.popleft()
            res.append(curr)
            q.append(curr+"0")
            q.append(curr+"1")
        return res