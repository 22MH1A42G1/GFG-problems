class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        if k == 0:
            return 0
        
        char_freq = {}
        max_length = -1
        left = 0
        
        for right in range(len(s)):
            if s[right] not in char_freq:
                char_freq[s[right]] = 0
            char_freq[s[right]] += 1
            
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1
            
            if len(char_freq)==k:
                max_length = max(max_length, right - left + 1)
        
        return max_length