class Solution:
    def isSumString(self, s: str) -> bool:
        """
        Time Complexity: O(n²)
        Space Complexity: O(n)
        Checks if a string is a sum-string where each number (after first two)
        is the sum of the two preceding numbers.
        """
        
        def add_strings(num1: str, num2: str) -> str:
            """Adds two numbers as strings to handle large numbers"""
            res = []
            i, j = len(num1) - 1, len(num2) - 1
            carry = 0
            while i >= 0 or j >= 0 or carry:
                d1 = int(num1[i]) if i >= 0 else 0
                d2 = int(num2[j]) if j >= 0 else 0
                total = d1 + d2 + carry
                carry = total // 10
                res.append(str(total % 10))
                i -= 1
                j -= 1
            return ''.join(reversed(res))
        
        memo = {}
        
        def check(pos: int, num1: str, num2: str) -> bool:
            """Recursively checks the sum property with memoization"""
            key = f"{pos},{num1},{num2}"
            if key in memo:
                return memo[key]
            
            # Base case: reached end of string
            if pos == len(s):
                memo[key] = True
                return True
            
            # Calculate expected next number
            next_num = add_strings(num1, num2)
            
            # Check if there's enough string left
            if pos + len(next_num) > len(s):
                memo[key] = False
                return False
            
            # Check if next part matches sum
            if s[pos:pos+len(next_num)] == next_num:
                result = check(pos + len(next_num), num2, next_num)
                memo[key] = result
                return result
            
            memo[key] = False
            return False
        
        n = len(s)
        if n < 3:
            return False
        
        # Try all possible initial splits (limited to 10 digits each)
        max_split_len = 10  # Set reasonable limit
        
        for len1 in range(1, min(n//2 + 1, max_split_len + 1)):
            num1 = s[:len1]
            
            # Skip numbers with leading zeros (unless "0")
            if len(num1) > 1 and num1[0] == '0':
                continue
                
            for len2 in range(1, min((n - len1)//2 + 1, max_split_len + 1)):
                num2 = s[len1:len1+len2]
                
                if len(num2) > 1 and num2[0] == '0':
                    continue
                
                # Check if remaining string follows pattern
                if check(len1 + len2, num1, num2):
                    return True
        
        return False