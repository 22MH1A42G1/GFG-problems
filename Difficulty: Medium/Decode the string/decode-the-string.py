class Solution:
    def decodedString(self, s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                st = ""
                while stack:
                    ele = stack.pop()
                    if ele == '[':
                        break
                    else:
                        st = ele + st
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                st = st * int(num)
                stack.append(st)
            else:
                stack.append(s[i])
            i += 1
        sol = ''
        while stack:
            sol = stack.pop() + sol
        return sol
