class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        word_set = set(dictionary)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        max_len = 0
        if dictionary:
            max_len = max(len(word) for word in dictionary)

        for i in range(1, n + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends