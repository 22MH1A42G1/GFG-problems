from collections import defaultdict
class TrieNode():
    
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.is_end=False
        
class Trie:
    
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        isValid=True
        curr=self.root
        for i in word[:-1]:
            curr=curr.children[i]
            if not curr.is_end:
                isValid=False
        curr=curr.children[word[-1]]
        curr.is_end=True
        return isValid

class Solution():
    def longestString(self, arr):
        trie=Trie()
        arr.sort()
        res=''
        for i in arr:
            if trie.insert(i) and len(i)>len(res):
                res=i
        return res