class Solution(object):
    
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            indices = []
            indices.append(i)
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    indices.append(j)
                    return indices