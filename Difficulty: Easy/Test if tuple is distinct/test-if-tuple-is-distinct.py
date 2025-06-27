#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"
print(len(arr)==len(set(arr)))
########### Write your code above ###############