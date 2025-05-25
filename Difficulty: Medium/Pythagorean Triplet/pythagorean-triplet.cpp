class Solution {
  public:
    bool pythagoreanTriplet(vector<int>& arr) {
        // code here
        unordered_map<int,int>mp;
        for(int i=0;i<arr.size();i++){
            mp[arr[i]*arr[i]]=i;
        }
        for(int i=0;i<arr.size();i++){
            for(int j=i+1;j<arr.size();j++){
                int reqd=arr[i]*arr[i]+arr[j]*arr[j];
                if(mp.find(reqd)!=mp.end() && mp[reqd]!=i && mp[reqd]!=j) return true; 
            }
        }
        return false;
    }
};