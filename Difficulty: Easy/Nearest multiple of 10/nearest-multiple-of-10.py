sys.set_int_max_str_digits(100000)

class Solution:
    def roundToNearest (self, Str) : 
        # Complete the function
        i = int(Str);
        rem = i%10
        low = i - rem
        high = low+10
        i = 0
        ans = ''
        while(Str[i] == '0'):
            ans += '0'
            i+=1
        if rem <=5:
                return ans+str(low)
        else:
                return ans+str(high)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends