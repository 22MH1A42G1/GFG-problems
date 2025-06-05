# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    return arr.append(ele)
# Function should pop an element from stack
def pop(arr):
    # Code here
    return arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return n==len(arr)

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return len(arr)==0

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    arr.sort()
    return arr[0]