class Solution {
  public:
    int catchThieves(vector<char> &arr, int k) {
        // Code here
         queue<int> police, thief;
        int count = 0;

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == 'P') police.push(i);
            else if (arr[i] == 'T') thief.push(i);

            while (!police.empty() && !thief.empty()) {
                if (abs(police.front() - thief.front()) <= k) {
                    count++;
                    police.pop(); thief.pop();
                } else if (thief.front() < police.front()) thief.pop();
                else police.pop();
            }
        }
        return count;
    }
};