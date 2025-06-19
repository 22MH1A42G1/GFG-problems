class Solution {
  public:
    string caseSort(string& s) {
        // code here
        string s1="",s2="",ans="";
        for(auto i:s){
            if(isupper(i)) s1+=i;
            else s2+=i;
        }
        sort(s1.begin(),s1.end());
        sort(s2.begin(),s2.end());
        int i=0,j=0;
        for(auto ch:s){
            if(isupper(ch)) ans+=s1[i++];
            else ans+=s2[j++];
        }
        return ans;
    }
};