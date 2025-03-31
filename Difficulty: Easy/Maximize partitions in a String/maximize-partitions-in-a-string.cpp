//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int maxPartitions(string &s) {
        // code here
        int n = s.size();
        
        vector<int> ans;
        vector<int> mp(26,-1);
        
        for(int i=0;i<n;i++){
            int idx = s[i] - 'a';
            mp[idx] = i;
        }
        
        int start = 0;
        int end = 0;
        int i = 0;
        
        while(i<n){
            end = max(end,mp[s[i] - 'a']);
            
            if(end == i){
                ans.push_back(end - start + 1);
                start = end + 1;
            }
            i++;
        }
        
        return ans.size();
        
    }
};


//{ Driver Code Starts.

int main() {
    int tc;
    cin >> tc;

    for (int i = 0; i < tc; ++i) {
        string s;
        cin >> s;
        Solution obj;
        cout << obj.maxPartitions(s) << endl;
        cout << "~" << endl;
    }

    return 0;
}

// } Driver Code Ends