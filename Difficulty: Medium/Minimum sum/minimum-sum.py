class Solution:
    def minSum(self, arr):
        # code here
        freqs = [0] * 10
        for d in arr:
            freqs[d] += 1
        _curr_digit = 9
        
        def get_digit():
            nonlocal _curr_digit
            while freqs[_curr_digit] == 0:
                _curr_digit -= 1
            freqs[_curr_digit] -= 1
            return _curr_digit
        
        n = len(arr) - freqs[0]
        output, carry = [], 0
        for _ in range(0, n - 1, 2):
            a, b = get_digit(), get_digit()
            carry, r = divmod(a + b + carry, 10)
            output.append(str(r))
        if n & 1:
            carry += get_digit()
        if carry:
            output.append(str(carry))
        return "".join(reversed(output))