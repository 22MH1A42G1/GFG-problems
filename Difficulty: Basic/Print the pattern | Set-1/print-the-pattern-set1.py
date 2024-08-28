def printPat(n):
    #Code here
    i = n
    while i > 0:
        j = n
        while j > 0:
            print((str(j) + ' ') * i, end='')
            j -= 1
        print("$", end="")
        i -= 1
        if i > 0:
            print("", end="")




#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        printPat(n)
        print()

# } Driver Code Ends