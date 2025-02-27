class Solution:

    def __init__(self):
        self.s=[]
        self.min_s=[]
        
    # Add an element to the top of Stack
    def push(self, x):
        self.s.append(x)
        if not self.min_s or x <= self.min_s[-1]:
            self.min_s.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if self.s:
            if self.s[-1] == self.min_s[-1]:  
                self.min_s.pop()  
            self.s.pop()

    # Returns top element of Stack
    def peek(self):
        if self.s:
            return self.s[-1]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        if self.min_s:
            return self.min_s[-1]
        return -1


#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends