#User function Template for python3
class trienode():
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        # implement Trie
        self.root = trienode()
        
    def insert(self, word: str):
       # insert word into Trie
       node = self.root
       for char in word:
           if char not in node.children:
               node.children[char] = trienode()
           node = node.children[char]
       node.is_end = True

    def search(self, word: str) -> bool:
         # search word in the Trie
         node = self.root
         for char in word:
             if char not in node.children:
                 return False
             node = node.children[char]
         return node.is_end

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
         node = self.root
         for char in word:
             if char not in node.children:
                 return False
             node = node.children[char]
         return True


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        ans = []
        trie = Trie()

        for _ in range(q):
            x, s = input().split()
            x = int(x)

            if x == 1:
                trie.insert(s)
            elif x == 2:
                ans.append(trie.search(s))
            elif x == 3:
                ans.append(trie.isPrefix(s))

        # Print results as lowercase true/false
        print(" ".join(["true" if res else "false" for res in ans]))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends