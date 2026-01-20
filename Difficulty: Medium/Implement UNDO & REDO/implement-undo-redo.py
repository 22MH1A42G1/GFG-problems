class Solution:
    def __init__(self):
        self.ans=[]
        self.st=[]
    def append(self, x):
        # append x into document
        self.ans.append(x)
        self.st.clear()
    def undo(self):
        # undo last change
        self.st.append(self.ans.pop())
    def redo(self):
        # redo changes
        self.ans.append(self.st.pop())
    def read(self):
        # read the document
        return "".join(self.ans)