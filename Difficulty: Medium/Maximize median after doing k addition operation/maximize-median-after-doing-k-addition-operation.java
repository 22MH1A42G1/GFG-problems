class Solution {
    public int maximizeMedian(int[] arr, int k) {
        int n = arr.length;
        Arrays.sort(arr);

        int medianIndex = (n - 1) / 2; 
        int res = arr[medianIndex];
        int l = arr[medianIndex];
        int r = arr[n - 1] + k;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (isPossible(arr, mid, n, k)) {
                res = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }

    private boolean isPossible(int[] arr, int mid, int n, int k) {
        long cost = 0;
        int half = n / 2;

        if (n % 2 == 0) {
            cost += Math.max(0L, (2L * mid) - arr[half] - arr[half - 1]);
            for (int i = half + 1; i < n; i++) {
                cost += Math.max(0L, mid - arr[i]);
            }
        } else {
            cost += Math.max(0L, mid - arr[half]);
            for (int i = half + 1; i < n; i++) {
                cost += Math.max(0L, mid - arr[i]);
            }
        }

        return cost <= k;
    }
}