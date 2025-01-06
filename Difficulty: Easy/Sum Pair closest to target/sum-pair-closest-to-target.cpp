//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
  public:
    vector<int> sumClosest(vector<int>& arr, int target) {
        sort(arr.begin(),arr.end());
        int i=0;int j=arr.size()-1;
        
        vector<int> ans;
        int mindiff = INT_MAX;
        
        
        while(i<j){
            int diff = (arr[i]+arr[j])-target;
            if(abs(diff) < mindiff){
                mindiff = min(abs(diff),mindiff);
                ans = vector<int> ({arr[i],arr[j]});
            }
            if(diff>0){
                j--;
            }else{
                i++;
            }
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
        int target = stoi(ks);
        Solution ob;
        vector<int> ans = ob.sumClosest(arr, target);
        if (ans.empty()) {
            cout << "[]";
        } else {
            for (auto it : ans) {
                cout << it << " ";
            }
        }
        cout << endl;
        cout << "~\n";
    }

    return 0;
}
// } Driver Code Ends