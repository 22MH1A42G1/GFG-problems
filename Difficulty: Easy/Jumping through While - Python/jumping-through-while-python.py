# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    i,j=1,1
    # Loop to jump in powers of 2
    while(i<=x):
        ##Your code here
        i=j*j
        if i<=x: print (i , end = " ")
        j+=1
        ##Your code here