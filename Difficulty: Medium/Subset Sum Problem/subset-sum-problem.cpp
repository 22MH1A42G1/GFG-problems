//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    bool solve(vector<int>&arr, int sum,int idx){
      if(idx > arr.size())return 0;
      if(sum < 0)return false;
      if(sum == 0)return 1;
      return solve(arr,sum - arr[idx],idx+1) || solve(arr,sum,idx+1);
    }
    bool isSubsetSum(vector<int>& arr, int sum) {
        // code here
        return solve(arr,sum,0);
    }
};


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        int sum;
        cin >> sum;
        cin.ignore();

        Solution ob;
        if (ob.isSubsetSum(arr, sum))
            cout << "true" << endl;
        else
            cout << "false" << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends