from collections import Counter, defaultdict
class Solution:

    def isPossible(self, arr, k):
        # Code here
        freq = Counter(arr)
        end = defaultdict(int)

        for num in arr:
            if freq[num] == 0:
                continue

            # Try to extend a previous subsequence
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
                freq[num] -= 1
            else:
                # Try to start a new subsequence of length k
                for next_num in range(num, num + k):
                    if freq[next_num] <= 0:
                        return False
                    freq[next_num] -= 1
                end[num + k - 1] += 1

        return True

