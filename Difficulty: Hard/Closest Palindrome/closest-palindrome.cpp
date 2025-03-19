//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    bool ispal(string s)
    {
        int i=0;
        int j=s.size()-1;
        while(i<j)
        {
            if(s[i]!=s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    long long int fun(long long int firstHalf,bool isEven)
    {
        long long resultNum=firstHalf;
        if(isEven==false)
        {
            firstHalf/=10;
        }
        while(firstHalf>0)
        {
            resultNum=resultNum*10+(firstHalf%10);
            firstHalf/=10;
        }
         return resultNum;
    }
    long long int closestPalindrome(long long int num){
        int len=log10(num)+1;
        if(num<10 || ispal(to_string(num))) return num;
        vector<long long int >possible_pal;
        string number=to_string(num);
        int mid=len/2;
        int firstHalfLength=(len%2==0) ? mid:(mid+1);
        long long int  firstHalf=stoll(number.substr(0,firstHalfLength));
        possible_pal.push_back(fun(firstHalf,len%2==0));
        possible_pal.push_back(fun(firstHalf+1,len%2==0));
        possible_pal.push_back(fun(firstHalf-1,len%2==0));
        possible_pal.push_back((long long int)pow(10,len-1)-1);
        possible_pal.push_back((long long int )pow(10,len)+1);
        
        
        long long int  result=1e9;
        long long int diff=1e9;
        for(int i=0;i<possible_pal.size();i++)
        {
            if(possible_pal[i]==num) continue;
            if(abs(num-possible_pal[i])<diff)
            {
                diff=abs(num-possible_pal[i]);
                result=possible_pal[i];
            }
            else if(diff==abs(num-possible_pal[i]))
            {
                result=min(result,possible_pal[i]);
            }
        }
        return result;
    }

};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		long long int num;
		cin >> num;
		Solution obj;
		long long int ans = obj.closestPalindrome(num);
		cout << ans <<"\n";
	
cout << "~" << "\n";
}
	return 0;
}
// } Driver Code Ends