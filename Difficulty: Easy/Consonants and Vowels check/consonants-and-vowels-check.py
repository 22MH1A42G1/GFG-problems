#User function Template for python3

def checkString(s):
    # write your code here
    v,c=0,0
    for i in range(len(s)):
        if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
            v += 1
        elif s[i]=="b" or s[i]=="c" or s[i]=="d" or s[i]=="f" or s[i]=="g" or s[i]=="h" or s[i]=="j" or s[i]=="k" or s[i]=="l" or s[i]=="m" or s[i]=="n" or s[i]=="p" or s[i]=="q" or s[i]=="r" or s[i]=="s" or s[i]=="t" or s[i]=="v" or s[i]=="w" or s[i]=="x" or s[i]=="y" or s[i] == "z":   
            c += 1
    if v>c: print("Yes")
    elif v<c: print("No")
    elif v==c: print("Same")

#{ 
 # Driver Code Starts

for _ in range(int(input())):
    s = input()
    checkString(s)
    print("~")
# } Driver Code Ends