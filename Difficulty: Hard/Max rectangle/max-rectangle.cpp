#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    // Find previous smaller elements
    vector<int> findPrevious(const vector<int>& arr) {
        stack<int> st;
        st.push(-1);
        vector<int> prev(arr.size());
        for (int i = 0; i < arr.size(); i++) {
            while (st.top() != -1 && arr[st.top()] >= arr[i]) {
                st.pop();
            }
            prev[i] = st.top();
            st.push(i);
        }
        return prev;
    }

    // Find next smaller elements
    vector<int> findNext(const vector<int>& arr) {
        stack<int> st;
        st.push(-1);
        vector<int> next(arr.size());
        for (int i = arr.size() - 1; i >= 0; i--) {
            while (st.top() != -1 && arr[st.top()] >= arr[i]) {
                st.pop();
            }
            next[i] = st.top();
            st.push(i);
        }
        return next;
    }

    // Calculate largest rectangle area in histogram
    int getMaxArea(const vector<int>& arr) {
        vector<int> prev = findPrevious(arr);
        vector<int> next = findNext(arr);
        int area = 0;
        for (int i = 0; i < arr.size(); i++) {
            int height = arr[i];
            if (next[i] == -1) next[i] = arr.size();
            int width = next[i] - prev[i] - 1;
            area = max(area, height * width);
        }
        return area;
    }

public:
    // Main function to calculate max rectangle area in binary matrix
    int maxArea(vector<vector<int>>& mat) {
        if (mat.empty() || mat[0].empty()) return 0;

        int maxArea = getMaxArea(mat[0]);

        for (int i = 1; i < mat.size(); i++) {
            for (int j = 0; j < mat[i].size(); j++) {
                if (mat[i][j] != 0) {
                    mat[i][j] += mat[i - 1][j];
                }
            }
            maxArea = max(maxArea, getMaxArea(mat[i]));
        }

        return maxArea;
    }
};
