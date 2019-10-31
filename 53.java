class Solution {
    public int maxSubArray(int[] nums) {
        int m = nums[0];
        for (int i = 0; i<nums.length; i++) {
            int now =nums[i];
            int prev = (i==0)? 0:nums[i-1];
            nums[i] = Math.max(now, prev+now);
            if (nums[i] > m) {m=nums[i];}
        }
        return m;
    }
}

Runtime: 1 ms, faster than 88.18% of Java online submissions for Maximum Subarray.
Memory Usage: 42.1 MB, less than 5.04% of Java online submissions for Maximum Subarray.



