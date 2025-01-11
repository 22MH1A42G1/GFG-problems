//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.HashMap;
import java.util.HashSet;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String s = read.readLine();
            Solution ob = new Solution();
            System.out.println(ob.longestUniqueSubstr(s));
            System.out.println("~");
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    public int longestUniqueSubstr(String s) {
        // code here
        int j =0;
        int ans=1;
        for (int i=0;i<s.length();i++){
            HashSet<Character> h1 = new HashSet<>();
            for (j=i;j<s.length();j++){
                char num = s.charAt(j);
                if (h1.contains(num)){
                    break;
                }
                else{
                    h1.add(num);
                }
            }
            ans = Math.max(ans,h1.size());
        }
        return ans;
    }
}