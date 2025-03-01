
class Solution:
    def decodedString(self, s):
        # code here
        st = []
        for i in range(len(s)):
            if s[i] != ']':
                st.append(s[i])
            else:
                temp = []
                while st and st[-1] != '[':
                    temp.append(st.pop())
                temp.reverse()
                st.pop()
                num = []
                while st and st[-1].isdigit():
                    num.insert(0, st.pop())
                number = int("".join(num))
                repeat = "".join(temp) * number
                st.extend(repeat)
        return "".join(st)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends