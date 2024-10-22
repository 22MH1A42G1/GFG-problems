//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    int sameOccurrence(vector<int>& arr, int x, int y) {
        // code here
        vector<int> temp = arr;
        for(auto &val:temp){
            if(val == x){
                val = 1;
            }
            else if(val == y){
                val = -1;
            }
            else{
                val = 0;
            }
        }
        map<int,int>mp;
        mp[0] = 1;
        int curr = 0;
        int ans = 0;
        int j=0;
        int n = arr.size();
        while(j < n){
            curr += temp[j];
            if(mp.find(curr) != mp.end()){
                ans += mp[curr];
            }
            mp[curr]++;
            j++;
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {

        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        string ks;
        getline(cin, ks);
        int x = stoi(ks);
        string ks1;
        getline(cin, ks1);
        int y = stoi(ks1);
        Solution ob;
        int ans = ob.sameOccurrence(arr, x, y);
        cout << ans << "\n";
        // cout<<"~"<<endl;
    }
    return 0;
}
// } Driver Code Ends