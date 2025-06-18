class Solution {
  public:
    vector<vector<string>> palinParts(string &s) {
        // code here
        vector<vector<string>> ans;
        vector<string> part;
        int l = s.length();
        findParts(0, l, s, part, ans);
        return ans;
    }
    void findParts(int i, int &l, string &s, vector<string> &part, vector<vector<string>> &ans) {
        if(i == l) {
            ans.push_back(part);
            return;
        }
        for(int j = i; j < l; j++) {
            if(checkPalin(s, i, j)) {
                part.push_back(s.substr(i, j-i+1));
                findParts(j+1, l, s, part, ans);
                part.pop_back();
            }
        }
    }
    bool checkPalin(string& s, int x, int y) {
        while(x < y)
            if(s[x++] != s[y--]) return false;
        return true;
    }
};