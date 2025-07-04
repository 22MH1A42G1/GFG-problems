# Function to check if pair
# with given sum exists
def pair_sum(dict, arr, sum):
    # code here
    # Hint: You can use 'in' to find if any key is in dict
    for i in range(len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==sum:
                return True
    return Fals